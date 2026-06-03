@echo off
echo.
echo   ================================
echo      Social AI - start (Windows)
echo   ================================
echo.

REM Sprawdz klucz API
if "%ANTHROPIC_API_KEY%"=="" (
    echo   Brak klucza ANTHROPIC_API_KEY!
    echo.
    set /p ANTHROPIC_API_KEY="  Wpisz klucz API (sk-ant-...): "
    echo.
)

echo   Instaluje zaleznosci Python...
cd /d "%~dp0backend"
pip install -r requirements.txt -q

echo.
echo   Uruchamiam serwer na http://localhost:8000
echo   Otworz przegladarke i wejdz na: http://localhost:8000
echo.
echo   Aby zatrzymac: Ctrl+C
echo.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
