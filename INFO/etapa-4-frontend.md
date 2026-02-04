# Etapa 4 - Frontend Next.js

## O que foi feito

Implementação de um frontend em Next.js 14 com tema dark e tons em verde água.

### Arquivos criados

```
frontend/
├── package.json         # Dependências do projeto
├── tsconfig.json        # Configuração TypeScript
├── next.config.js       # Configuração Next.js (proxy para API)
├── next-env.d.ts        # Types do Next.js
└── src/
    ├── app/
    │   ├── globals.css  # Estilos globais (tema dark)
    │   ├── layout.tsx   # Layout principal
    │   └── page.tsx     # Página principal
    └── lib/
        └── api.ts       # Funções de acesso à API
```

---

## Funcionalidades

### Abas de Navegação
- **Treinadores** - CRUD de treinadores
- **Pokémons** - CRUD de pokémon
- **Batalhas** - Simulação de batalhas

### Operações por Aba

| Aba | Criar | Consultar | Deletar |
|-----|-------|-----------|---------|
| Treinadores | ✅ | ✅ (por ID ou todos) | ✅ |
| Pokémons | ✅ | ✅ (por ID ou todos) | ✅ |
| Batalhas | - | - | - |

---

## Design

- **Tema:** Dark mode
- **Cor principal:** Verde água (#2dd4bf)
- **Layout:** Centralizado, responsivo
- **Feedback:** Mensagens de sucesso/erro

---

## Como Executar

### 1. Instalar dependências

```bash
cd frontend
npm install
```

### 2. Iniciar API (backend)

```bash
# Em outro terminal, na pasta raiz
uvicorn app.main:app --reload --port 8000
```

### 3. Iniciar frontend

```bash
cd frontend
npm run dev
```

### 4. Acessar

- Frontend: http://localhost:3000
- API: http://localhost:8000

---

## Proxy de API

O `next.config.js` configura um proxy para redirecionar chamadas `/api/*` para o backend:

```javascript
async rewrites() {
  return [
    {
      source: '/api/:path*',
      destination: 'http://localhost:8000/:path*'
    }
  ]
}
```

Isso evita problemas de CORS durante o desenvolvimento.

---

## Build para Produção

```bash
cd frontend
npm run build
npm start
```
