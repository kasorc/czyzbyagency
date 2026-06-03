# Social AI – Panel zarządzania social mediami

Panel dla 3 marek: **Zimowa Akademia**, **3x3 Koszykówka**, **bdb event**

## Struktura projektu

```
social-ai/
├── backend/
│   ├── main.py              # FastAPI serwer
│   └── requirements.txt     # Zależności Python
├── frontend/
│   └── index.html           # Aplikacja (jeden plik)
├── start.sh                 # Skrypt startowy (Mac/Linux)
├── start.bat                # Skrypt startowy (Windows)
└── README.md
```

---

## Instalacja i uruchomienie

### Wymagania
- Python 3.10 lub nowszy
- Klucz API Anthropic (https://console.anthropic.com)

---

### Mac / Linux

```bash
# 1. Wejdź do folderu projektu
cd social-ai

# 2. Ustaw klucz API
export ANTHROPIC_API_KEY="sk-ant-twój-klucz-tutaj"

# 3. Uruchom
bash start.sh
```

### Windows

```bat
REM 1. Otwórz Command Prompt i wejdź do folderu
cd social-ai

REM 2. Ustaw klucz API
set ANTHROPIC_API_KEY=sk-ant-twój-klucz-tutaj

REM 3. Uruchom
start.bat
```

### Ręcznie (bez skryptu)

```bash
cd social-ai/backend
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Po uruchomieniu otwórz przeglądarkę: **http://localhost:8000**

---

## Gdzie znaleźć klucz API

1. Wejdź na https://console.anthropic.com
2. Zaloguj się lub zarejestruj
3. Przejdź do **API Keys**
4. Kliknij **Create Key**
5. Skopiuj klucz (zaczyna się od `sk-ant-`)

---

## Funkcje

| Moduł | Opis |
|---|---|
| **Generator postów** | Generuje posty FB, Instagram lub wpis na bloga |
| **Uczenie agenta** | 10 postów do oceny – agent zapamiętuje preferencje |
| **Baza eventów** | Zapisane eventy z licznikiem dni do startu |
| **Baza wiedzy** | Edytowalne profile każdej marki (ton, oferta, hashtagi) |
| **Historia** | Wszystkie wygenerowane posty z ocenami |
| **Skrzynka bdb** | Przepisuje posty z Zimowej/3x3 na język B2B |

---

## Trwała pamięć

Wszystkie dane (eventy, feedback, historia, baza wiedzy) są zapisywane w **localStorage** przeglądarki – przeżywają odświeżenie strony. Działają na jednym urządzeniu i przeglądarce.

Aby synchronizować między urządzeniami – potrzebna baza danych (np. PostgreSQL). Skontaktuj się z programistą.

---

## Wdrożenie na serwer (produkcja)

```bash
# Zainstaluj na serwerze Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip -y

# Sklonuj / wgraj pliki na serwer
# Ustaw klucz API jako zmienną środowiskową systemu

# Uruchom z gunicorn (stabilniejszy niż uvicorn dev)
pip install gunicorn
gunicorn main:app -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

Zalecane jest użycie **nginx** jako reverse proxy przed gunicornem.

---

## Rozwiązywanie problemów

**Backend niedostępny** – upewnij się że serwer działa (`uvicorn` uruchomiony) i otwierasz http://localhost:8000

**Brak klucza API** – sprawdź czy zmienna `ANTHROPIC_API_KEY` jest ustawiona: `echo $ANTHROPIC_API_KEY`

**Port zajęty** – zmień port: `uvicorn main:app --port 8001`
