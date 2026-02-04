"""
Entry point para Vercel Serverless Functions.
Exporta o app FastAPI para ser usado como handler.
"""
from app.main import app

# Vercel espera o app FastAPI diretamente
app = app
