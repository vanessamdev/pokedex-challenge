'use client'

import { useState } from 'react'
import * as api from '@/lib/api'

type Tab = 'treinadores' | 'pokemons' | 'batalhas'

export default function Home() {
  const [activeTab, setActiveTab] = useState<Tab>('treinadores')
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null)
  const [loading, setLoading] = useState(false)

  // Trainers state
  const [trainers, setTrainers] = useState<api.Trainer[]>([])
  const [trainerName, setTrainerName] = useState('')
  const [trainerId, setTrainerId] = useState('')

  // Pokemon state
  const [pokemons, setPokemons] = useState<api.Pokemon[]>([])
  const [pokemonName, setPokemonName] = useState('')
  const [pokemonType, setPokemonType] = useState('')
  const [pokemonLevel, setPokemonLevel] = useState('')
  const [pokemonTrainerId, setPokemonTrainerId] = useState('')
  const [pokemonId, setPokemonId] = useState('')

  // Battle state
  const [attackerId, setAttackerId] = useState('')
  const [defenderId, setDefenderId] = useState('')
  const [battleResult, setBattleResult] = useState<api.BattleResult | null>(null)

  const showMessage = (type: 'success' | 'error', text: string) => {
    setMessage({ type, text })
    setTimeout(() => setMessage(null), 3000)
  }

  // Trainer handlers
  const handleListTrainers = async () => {
    setLoading(true)
    try {
      const data = await api.getTrainers()
      setTrainers(data)
      if (data.length === 0) showMessage('success', 'Nenhum treinador cadastrado')
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleSearchTrainer = async () => {
    if (!trainerId) return showMessage('error', 'Informe o ID do treinador')
    setLoading(true)
    try {
      const data = await api.getTrainer(Number(trainerId))
      setTrainers([data])
    } catch (err: any) {
      showMessage('error', err.message)
      setTrainers([])
    }
    setLoading(false)
  }

  const handleCreateTrainer = async () => {
    if (!trainerName) return showMessage('error', 'Informe o nome do treinador')
    setLoading(true)
    try {
      await api.createTrainer(trainerName)
      showMessage('success', 'Treinador criado com sucesso!')
      setTrainerName('')
      handleListTrainers()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleDeleteTrainer = async () => {
    if (!trainerId) return showMessage('error', 'Informe o ID do treinador')
    setLoading(true)
    try {
      await api.deleteTrainer(Number(trainerId))
      showMessage('success', 'Treinador deletado com sucesso!')
      setTrainerId('')
      handleListTrainers()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleUpdateTrainer = async () => {
    if (!trainerId || !trainerName) return showMessage('error', 'Informe o ID e o novo nome do treinador')
    setLoading(true)
    try {
      await api.updateTrainer(Number(trainerId), trainerName)
      showMessage('success', 'Treinador atualizado com sucesso!')
      setTrainerName('')
      setTrainerId('')
      handleListTrainers()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  // Pokemon handlers
  const handleListPokemons = async () => {
    setLoading(true)
    try {
      const data = await api.getPokemons()
      setPokemons(data)
      if (data.length === 0) showMessage('success', 'Nenhum pokémon cadastrado')
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleSearchPokemon = async () => {
    if (!pokemonId) return showMessage('error', 'Informe o ID do pokémon')
    setLoading(true)
    try {
      const data = await api.getPokemon(Number(pokemonId))
      setPokemons([data])
    } catch (err: any) {
      showMessage('error', err.message)
      setPokemons([])
    }
    setLoading(false)
  }

  const handleCreatePokemon = async () => {
    if (!pokemonName || !pokemonType || !pokemonLevel || !pokemonTrainerId) {
      return showMessage('error', 'Preencha todos os campos')
    }
    setLoading(true)
    try {
      await api.createPokemon({
        nome: pokemonName,
        tipo: pokemonType,
        nivel: Number(pokemonLevel),
        treinador_id: Number(pokemonTrainerId)
      })
      showMessage('success', 'Pokémon criado com sucesso!')
      setPokemonName('')
      setPokemonType('')
      setPokemonLevel('')
      setPokemonTrainerId('')
      handleListPokemons()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleDeletePokemon = async () => {
    if (!pokemonId) return showMessage('error', 'Informe o ID do pokémon')
    setLoading(true)
    try {
      await api.deletePokemon(Number(pokemonId))
      showMessage('success', 'Pokémon deletado com sucesso!')
      setPokemonId('')
      handleListPokemons()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  const handleUpdatePokemon = async () => {
    if (!pokemonId) return showMessage('error', 'Informe o ID do pokémon')
    if (!pokemonName && !pokemonType && !pokemonLevel) {
      return showMessage('error', 'Informe pelo menos um campo para atualizar')
    }
    setLoading(true)
    try {
      const data: { nome?: string; tipo?: string; nivel?: number } = {}
      if (pokemonName) data.nome = pokemonName
      if (pokemonType) data.tipo = pokemonType
      if (pokemonLevel) data.nivel = Number(pokemonLevel)
      
      await api.updatePokemon(Number(pokemonId), data)
      showMessage('success', 'Pokémon atualizado com sucesso!')
      setPokemonName('')
      setPokemonType('')
      setPokemonLevel('')
      setPokemonId('')
      handleListPokemons()
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  // Battle handler
  const handleBattle = async () => {
    if (!attackerId || !defenderId) {
      return showMessage('error', 'Informe os IDs dos dois pokémon')
    }
    setLoading(true)
    setBattleResult(null)
    try {
      const result = await api.battle(Number(attackerId), Number(defenderId))
      setBattleResult(result)
    } catch (err: any) {
      showMessage('error', err.message)
    }
    setLoading(false)
  }

  return (
    <div className="container">
      <h1 className="title">🎮 Pokédex API</h1>

      {/* Navigation Tabs */}
      <div className="nav-tabs">
        <button
          className={`nav-tab ${activeTab === 'treinadores' ? 'active' : ''}`}
          onClick={() => { setActiveTab('treinadores'); setTrainers([]) }}
        >
          Treinadores
        </button>
        <button
          className={`nav-tab ${activeTab === 'pokemons' ? 'active' : ''}`}
          onClick={() => { setActiveTab('pokemons'); setPokemons([]) }}
        >
          Pokémons
        </button>
        <button
          className={`nav-tab ${activeTab === 'batalhas' ? 'active' : ''}`}
          onClick={() => { setActiveTab('batalhas'); setBattleResult(null) }}
        >
          Batalhas
        </button>
      </div>

      {/* Message */}
      {message && (
        <div className={`message ${message.type}`}>{message.text}</div>
      )}

      {/* Trainers Tab */}
      {activeTab === 'treinadores' && (
        <>
          <div className="form-section">
            <div className="input-group">
              <label>Nome do Treinador</label>
              <input
                type="text"
                className="input-field"
                placeholder="Ex: Ash Ketchum"
                value={trainerName}
                onChange={(e) => setTrainerName(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>ID do Treinador (para consulta/atualização/exclusão)</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 1"
                value={trainerId}
                onChange={(e) => setTrainerId(e.target.value)}
              />
            </div>
            <div className="action-buttons">
              <button className="btn btn-primary" onClick={handleCreateTrainer} disabled={loading}>
                Criar
              </button>
              <button className="btn btn-secondary" onClick={trainerId ? handleSearchTrainer : handleListTrainers} disabled={loading}>
                Consultar
              </button>
              <button className="btn btn-warning" onClick={handleUpdateTrainer} disabled={loading}>
                Atualizar
              </button>
              <button className="btn btn-danger" onClick={handleDeleteTrainer} disabled={loading}>
                Deletar
              </button>
            </div>
          </div>

          <div className="results-section">
            {loading && <div className="loading">Carregando...</div>}
            {!loading && trainers.length === 0 && (
              <div className="empty-state">Clique em Consultar para listar os treinadores</div>
            )}
            {trainers.map((trainer) => (
              <div key={trainer.id} className="result-card">
                <h3>{trainer.nome}</h3>
                <p><span className="id-badge">ID: {trainer.id}</span></p>
              </div>
            ))}
          </div>
        </>
      )}

      {/* Pokemon Tab */}
      {activeTab === 'pokemons' && (
        <>
          <div className="form-section">
            <div className="input-group">
              <label>Nome do Pokémon</label>
              <input
                type="text"
                className="input-field"
                placeholder="Ex: Pikachu"
                value={pokemonName}
                onChange={(e) => setPokemonName(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>Tipo</label>
              <input
                type="text"
                className="input-field"
                placeholder="Ex: Elétrico, Fogo, Água, Planta"
                value={pokemonType}
                onChange={(e) => setPokemonType(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>Nível</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 10"
                value={pokemonLevel}
                onChange={(e) => setPokemonLevel(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>ID do Treinador</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 1"
                value={pokemonTrainerId}
                onChange={(e) => setPokemonTrainerId(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>ID do Pokémon (para consulta/atualização/exclusão)</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 1"
                value={pokemonId}
                onChange={(e) => setPokemonId(e.target.value)}
              />
            </div>
            <div className="action-buttons">
              <button className="btn btn-primary" onClick={handleCreatePokemon} disabled={loading}>
                Criar
              </button>
              <button className="btn btn-secondary" onClick={pokemonId ? handleSearchPokemon : handleListPokemons} disabled={loading}>
                Consultar
              </button>
              <button className="btn btn-warning" onClick={handleUpdatePokemon} disabled={loading}>
                Atualizar
              </button>
              <button className="btn btn-danger" onClick={handleDeletePokemon} disabled={loading}>
                Deletar
              </button>
            </div>
          </div>

          <div className="results-section">
            {loading && <div className="loading">Carregando...</div>}
            {!loading && pokemons.length === 0 && (
              <div className="empty-state">Clique em Consultar para listar os pokémon</div>
            )}
            {pokemons.map((pokemon) => (
              <div key={pokemon.id} className="result-card">
                <h3>{pokemon.nome}</h3>
                <p><span className="id-badge">ID: {pokemon.id}</span> Tipo: {pokemon.tipo}</p>
                <p>Nível: {pokemon.nivel} | Treinador ID: {pokemon.treinador_id}</p>
              </div>
            ))}
          </div>
        </>
      )}

      {/* Battle Tab */}
      {activeTab === 'batalhas' && (
        <>
          <div className="form-section">
            <div className="input-group">
              <label>ID do Pokémon Atacante</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 1"
                value={attackerId}
                onChange={(e) => setAttackerId(e.target.value)}
              />
            </div>
            <div className="input-group">
              <label>ID do Pokémon Defensor</label>
              <input
                type="number"
                className="input-field"
                placeholder="Ex: 2"
                value={defenderId}
                onChange={(e) => setDefenderId(e.target.value)}
              />
            </div>
            <div className="action-buttons">
              <button className="btn btn-primary" onClick={handleBattle} disabled={loading}>
                ⚔️ Batalhar!
              </button>
            </div>
          </div>

          {/* Battle Result */}
          {battleResult && (
            <div className={`battle-result ${battleResult.resultado}`}>
              {battleResult.resultado === 'vitoria' ? (
                <>
                  <h2>🏆 Vitória!</h2>
                  <p className="winner">Vencedor: {battleResult.vencedor?.nome}</p>
                  <p className="loser">Perdedor: {battleResult.perdedor?.nome}</p>
                </>
              ) : (
                <>
                  <h2>🤝 Empate!</h2>
                  <p>{battleResult.mensagem}</p>
                </>
              )}
            </div>
          )}
        </>
      )}
    </div>
  )
}
