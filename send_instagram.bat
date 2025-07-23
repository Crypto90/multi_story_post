@echo off
setlocal

REM === Activate Python environment if needed ===
REM call path\to\venv\Scripts\activate

REM === Run your scripts ===
python upload_instagram.py

echo ✅ All scripts completed.
endlocal
pause
