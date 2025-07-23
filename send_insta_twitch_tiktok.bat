@echo off
setlocal

REM === Check for BlueStacks process ===
tasklist /FI "IMAGENAME eq HD-Player.exe" | find /I "HD-Player.exe" >nul
if errorlevel 1 (
    echo ❌ BlueStacks is NOT running. Aborting.
    exit /b 1
)

echo ✅ BlueStacks is running. Starting uploads...

REM === Activate Python environment if needed ===
REM call path\to\venv\Scripts\activate

REM === Run your scripts ===
python upload_instagram.py
python upload_twitch.py
python upload_tiktok.py

echo ✅ All scripts completed.
endlocal
pause
