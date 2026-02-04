# Checklist - Apresentação do Projeto Pokédex API

## Pré-requisitos na Máquina de Apresentação

- [ ] Python 3.12+ instalado
- [ ] Node.js 18+ instalado
- [ ] npm instalado
- [ ] Projeto copiado/clonado

---

## Preparação (antes da apresentação)

### 1. Instalar Dependências

```bash
# Na pasta raiz do projeto
cd pokedex-challenge

# Dependências Node (Serverless)
npm install

# Dependências Python
pip install -r requirements.txt
```

### 2. Verificar Arquivos Importantes

- [ ] `serverless.yml` - Configuração Serverless
- [ ] `package.json` - Dependências Node
- [ ] `requirements.txt` - Dependências Python
- [ ] `app/` - Código do backend
- [ ] `frontend/` - Código do frontend
- [ ] `frontend/public/background.png` - Imagem de fundo

---

## Execução

### Opção 1: Serverless Offline (Recomendado para apresentação)

```bash
# Terminal 1 - Backend Serverless
serverless offline
# ou
npm run offline
```
**API:** http://localhost:3000

### Opção 2: Uvicorn (Alternativa)

```bash
# Terminal 1 - Backend
uvicorn app.main:app --reload --port 8000
```
**API:** http://localhost:8000

### Frontend

```bash
# Terminal 2 - Frontend
cd frontend
npm install
npm run dev -- -p 3001
```
**Frontend:** http://localhost:3001

---

## Verificação Rápida

### Testar Backend

```bash
# Criar treinador
curl -X POST http://localhost:3000/treinadores -H "Content-Type: application/json" -d '{"nome": "Ash"}'

# Listar treinadores
curl http://localhost:3000/treinadores
```

### Acessar Documentação

- Swagger: http://localhost:3000/docs
- ReDoc: http://localhost:3000/redoc

---

## Demonstração Sugerida

### 1. Mostrar Arquitetura (2 min)
- [ ] Estrutura de pastas SOLID
- [ ] Explicar separação: interfaces → repositories → services

### 2. Backend - Swagger (3 min)
- [ ] Acessar http://localhost:3000/docs
- [ ] Criar treinador
- [ ] Criar pokémon
- [ ] Listar pokémon do treinador

### 3. Frontend (3 min)
- [ ] Mostrar interface dark com background
- [ ] Criar treinador via interface
- [ ] Criar pokémon
- [ ] Atualizar pokémon
- [ ] Simular batalha

### 4. Batalha (2 min)
- [ ] Criar 2 pokémon com tipos diferentes
- [ ] Demonstrar regra de nível
- [ ] Demonstrar regra de tipo (Fogo > Planta)
- [ ] Mostrar empate

---

## Troubleshooting

### Erro: "porta em uso"
```bash
# Windows - matar processo na porta
Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Stop-Process -Force
```

### Erro: "módulo não encontrado"
```bash
pip install -r requirements.txt
npm install
```

### Erro: "CORS"
- Verificar se backend está rodando
- Verificar porta no `frontend/src/lib/api.ts`

### Frontend não conecta ao backend
Editar `frontend/src/lib/api.ts`:
```typescript
const API_URL = 'http://localhost:3000'  // Ajustar porta
```

---

## URLs Importantes

| Serviço | URL |
|---------|-----|
| Backend (Serverless) | http://localhost:3000 |
| Backend (Uvicorn) | http://localhost:8000 |
| Frontend | http://localhost:3001 |
| Swagger | http://localhost:3000/docs |
| ReDoc | http://localhost:3000/redoc |
