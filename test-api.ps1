# Script de testes da API (Windows PowerShell)
# Uso: .\test-api.ps1
# Certifique-se que o backend está rodando antes de executar

param(
    [string]$BaseUrl = "http://localhost:8000"
)

Write-Host "=== Testando API Pokedex ===" -ForegroundColor Cyan
Write-Host "URL Base: $BaseUrl" -ForegroundColor Gray
Write-Host ""

$passed = 0
$failed = 0

function Test-Endpoint {
    param($Name, $Method, $Url, $Body)
    
    Write-Host "Testando: $Name" -ForegroundColor Yellow
    try {
        if ($Body) {
            $response = Invoke-RestMethod -Uri $Url -Method $Method -ContentType "application/json" -Body $Body
        } else {
            $response = Invoke-RestMethod -Uri $Url -Method $Method
        }
        Write-Host "  OK" -ForegroundColor Green
        $script:passed++
        return $response
    } catch {
        Write-Host "  ERRO: $($_.Exception.Message)" -ForegroundColor Red
        $script:failed++
        return $null
    }
}

# ============ TESTES ============

Write-Host "--- TREINADORES ---" -ForegroundColor Magenta

# Criar treinador
$trainer = Test-Endpoint "Criar Treinador" "POST" "$BaseUrl/treinadores" '{"nome": "Ash Ketchum"}'
$trainerId = $trainer.id

# Listar treinadores
Test-Endpoint "Listar Treinadores" "GET" "$BaseUrl/treinadores"

# Buscar treinador
if ($trainerId) {
    Test-Endpoint "Buscar Treinador" "GET" "$BaseUrl/treinadores/$trainerId"
}

Write-Host ""
Write-Host "--- POKEMONS ---" -ForegroundColor Magenta

# Criar pokémon
if ($trainerId) {
    $pokemon1 = Test-Endpoint "Criar Pokemon 1 (Fogo)" "POST" "$BaseUrl/pokemons" "{`"nome`": `"Charmander`", `"tipo`": `"Fogo`", `"nivel`": 10, `"treinador_id`": $trainerId}"
    $pokemon2 = Test-Endpoint "Criar Pokemon 2 (Agua)" "POST" "$BaseUrl/pokemons" "{`"nome`": `"Squirtle`", `"tipo`": `"Agua`", `"nivel`": 10, `"treinador_id`": $trainerId}"
    $pokemon3 = Test-Endpoint "Criar Pokemon 3 (Planta)" "POST" "$BaseUrl/pokemons" "{`"nome`": `"Bulbasaur`", `"tipo`": `"Planta`", `"nivel`": 8, `"treinador_id`": $trainerId}"
}

# Listar pokémon
Test-Endpoint "Listar Pokemons" "GET" "$BaseUrl/pokemons"

# Listar pokémon do treinador
if ($trainerId) {
    Test-Endpoint "Listar Pokemons do Treinador" "GET" "$BaseUrl/treinadores/$trainerId/pokemons"
}

Write-Host ""
Write-Host "--- BATALHAS ---" -ForegroundColor Magenta

# Batalha por tipo (Fogo vs Planta - Fogo vence)
if ($pokemon1 -and $pokemon3) {
    Write-Host "Batalha: Charmander (Fogo) vs Bulbasaur (Planta)" -ForegroundColor Gray
    Test-Endpoint "Batalha Fogo vs Planta" "POST" "$BaseUrl/batalhas" "{`"pokemon_atacante_id`": $($pokemon1.id), `"pokemon_defensor_id`": $($pokemon3.id)}"
}

# Batalha por tipo (Agua vs Fogo - Agua vence)
if ($pokemon2 -and $pokemon1) {
    Write-Host "Batalha: Squirtle (Agua) vs Charmander (Fogo)" -ForegroundColor Gray
    Test-Endpoint "Batalha Agua vs Fogo" "POST" "$BaseUrl/batalhas" "{`"pokemon_atacante_id`": $($pokemon2.id), `"pokemon_defensor_id`": $($pokemon1.id)}"
}

Write-Host ""
Write-Host "--- DELETE ---" -ForegroundColor Magenta

# Deletar pokémon
if ($pokemon3) {
    Test-Endpoint "Deletar Pokemon" "DELETE" "$BaseUrl/pokemons/$($pokemon3.id)"
}

Write-Host ""
Write-Host "=== RESULTADO ===" -ForegroundColor Cyan
Write-Host "Passou: $passed" -ForegroundColor Green
Write-Host "Falhou: $failed" -ForegroundColor Red

if ($failed -eq 0) {
    Write-Host ""
    Write-Host "Todos os testes passaram!" -ForegroundColor Green
}
