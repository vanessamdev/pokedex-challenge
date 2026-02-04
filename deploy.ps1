# Script de deploy para AWS Lambda
# Execute: .\deploy.ps1

Write-Host "=== Preparando pacote para deploy ===" -ForegroundColor Cyan

# Criar pasta temporária
$buildDir = "build"
if (Test-Path $buildDir) {
    Remove-Item -Recurse -Force $buildDir
}
New-Item -ItemType Directory -Path $buildDir | Out-Null

# Instalar dependências na pasta build
Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt -t $buildDir --quiet

# Copiar código da aplicação
Write-Host "Copiando codigo da aplicacao..." -ForegroundColor Yellow
Copy-Item -Recurse "app" "$buildDir/app"

# Criar arquivo ZIP
Write-Host "Criando pacote ZIP..." -ForegroundColor Yellow
$zipFile = "pokedex-api.zip"
if (Test-Path $zipFile) {
    Remove-Item $zipFile
}
Compress-Archive -Path "$buildDir/*" -DestinationPath $zipFile

# Limpar pasta temporária
Remove-Item -Recurse -Force $buildDir

Write-Host "=== Pacote criado: $zipFile ===" -ForegroundColor Green
Write-Host ""
Write-Host "Proximos passos:" -ForegroundColor Cyan
Write-Host "1. Instale o Serverless Framework: npm install -g serverless"
Write-Host "2. Configure AWS credentials: serverless config credentials --provider aws --key <KEY> --secret <SECRET>"
Write-Host "3. Deploy: serverless deploy"
Write-Host ""
Write-Host "Ou faca upload manual do ZIP no AWS Lambda Console"
