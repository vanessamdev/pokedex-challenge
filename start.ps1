# Script para iniciar o projeto completo (Windows PowerShell)
# Uso: .\start.ps1

Write-Host "=== Iniciando Pokedex API ===" -ForegroundColor Cyan

# Verificar se está na pasta correta
if (-not (Test-Path "app/main.py")) {
    Write-Host "Erro: Execute este script na pasta raiz do projeto" -ForegroundColor Red
    exit 1
}

# Ativar venv se existir
if (Test-Path "venv/Scripts/Activate.ps1") {
    Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
    & ./venv/Scripts/Activate.ps1
}

# Iniciar backend em background
Write-Host "Iniciando Backend (porta 8000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; ./venv/Scripts/Activate.ps1; uvicorn app.main:app --reload --port 8000"

# Aguardar backend iniciar
Start-Sleep -Seconds 3

# Iniciar frontend
Write-Host "Iniciando Frontend (porta 3000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD/frontend'; npm run dev"

Write-Host ""
Write-Host "=== Projeto Iniciado ===" -ForegroundColor Green
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
