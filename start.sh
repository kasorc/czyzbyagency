#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  Social AI – skrypt startowy
#  Uruchom: bash start.sh
# ─────────────────────────────────────────────────────────────

echo ""
echo "  ╔═══════════════════════════════╗"
echo "  ║      Social AI – start        ║"
echo "  ╚═══════════════════════════════╝"
echo ""

# Sprawdź klucz API
if [ -z "$ANTHROPIC_API_KEY" ]; then
  echo "  ⚠️  Brak klucza ANTHROPIC_API_KEY!"
  echo ""
  echo "  Ustaw go przed uruchomieniem:"
  echo "  export ANTHROPIC_API_KEY='sk-ant-...'"
  echo ""
  read -p "  Lub wpisz klucz teraz: " key
  export ANTHROPIC_API_KEY="$key"
fi

# Instalacja zależności
echo ""
echo "  📦 Instaluję zależności Python..."
cd "$(dirname "$0")/backend"
pip install -r requirements.txt -q

# Start serwera
echo ""
echo "  🚀 Uruchamiam serwer na http://localhost:8000"
echo "  Otwórz przeglądarkę i wejdź na: http://localhost:8000"
echo ""
echo "  Aby zatrzymać: Ctrl+C"
echo ""

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
