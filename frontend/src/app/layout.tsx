import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Pokédex API',
  description: 'Gerenciamento de Treinadores e Pokémon',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  )
}
