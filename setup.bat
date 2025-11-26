@echo off
REM Setup script for Autoclicker Python version (Windows)

echo Autoclicker Setup
echo =================
echo.

REM Check Python version
python --version
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete!
echo.
echo To run the autoclicker:
echo   python autoclicker.py
echo.
pause
