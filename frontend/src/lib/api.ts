// ============ CONFIGURAÇÃO ORIGINAL (desenvolvimento local) ============
// const API_URL = 'http://localhost:3000'

// ============ CONFIGURAÇÃO VERCEL (produção) ============
// Em produção na Vercel, a API está no mesmo domínio (string vazia)
// Em desenvolvimento local, usa localhost:8000 (uvicorn)
const API_URL = process.env.NEXT_PUBLIC_API_URL || ''

// Types
export interface Trainer {
  id: number
  nome: string
}

export interface Pokemon {
  id: number
  nome: string
  tipo: string
  nivel: number
  treinador_id: number
}

export interface BattleResult {
  resultado: 'vitoria' | 'empate'
  vencedor?: { id: number; nome: string }
  perdedor?: { id: number; nome: string }
  mensagem?: string
}

// Trainers API
export async function getTrainers(): Promise<Trainer[]> {
  const res = await fetch(`${API_URL}/treinadores`)
  if (!res.ok) throw new Error('Erro ao buscar treinadores')
  return res.json()
}

export async function getTrainer(id: number): Promise<Trainer> {
  const res = await fetch(`${API_URL}/treinadores/${id}`)
  if (!res.ok) throw new Error('Treinador não encontrado')
  return res.json()
}

export async function createTrainer(nome: string): Promise<Trainer> {
  const res = await fetch(`${API_URL}/treinadores`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome })
  })
  if (!res.ok) throw new Error('Erro ao criar treinador')
  return res.json()
}

export async function deleteTrainer(id: number): Promise<void> {
  const res = await fetch(`${API_URL}/treinadores/${id}`, { method: 'DELETE' })
  if (!res.ok) throw new Error('Erro ao deletar treinador')
}

export async function updateTrainer(id: number, nome: string): Promise<Trainer> {
  const res = await fetch(`${API_URL}/treinadores/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome })
  })
  if (!res.ok) throw new Error('Erro ao atualizar treinador')
  return res.json()
}

// Pokemon API
export async function getPokemons(): Promise<Pokemon[]> {
  const res = await fetch(`${API_URL}/pokemons`)
  if (!res.ok) throw new Error('Erro ao buscar pokémon')
  return res.json()
}

export async function getPokemon(id: number): Promise<Pokemon> {
  const res = await fetch(`${API_URL}/pokemons/${id}`)
  if (!res.ok) throw new Error('Pokémon não encontrado')
  return res.json()
}

export async function createPokemon(data: {
  nome: string
  tipo: string
  nivel: number
  treinador_id: number
}): Promise<Pokemon> {
  const res = await fetch(`${API_URL}/pokemons`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  if (!res.ok) {
    const error = await res.json()
    throw new Error(error.detail || 'Erro ao criar pokémon')
  }
  return res.json()
}

export async function deletePokemon(id: number): Promise<void> {
  const res = await fetch(`${API_URL}/pokemons/${id}`, { method: 'DELETE' })
  if (!res.ok) throw new Error('Erro ao deletar pokémon')
}

export async function updatePokemon(id: number, data: {
  nome?: string
  tipo?: string
  nivel?: number
}): Promise<Pokemon> {
  const res = await fetch(`${API_URL}/pokemons/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  if (!res.ok) throw new Error('Erro ao atualizar pokémon')
  return res.json()
}

// Battle API
export async function battle(atacanteId: number, defensorId: number): Promise<BattleResult> {
  const res = await fetch(`${API_URL}/batalhas`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      pokemon_atacante_id: atacanteId,
      pokemon_defensor_id: defensorId
    })
  })
  if (!res.ok) {
    const error = await res.json()
    throw new Error(error.detail || 'Erro na batalha')
  }
  return res.json()
}
