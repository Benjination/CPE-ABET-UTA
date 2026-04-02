@echo off
REM Build script for ABET CPE Course Mapping System (Windows)
REM Creates a standalone executable for Windows

setlocal

echo ==========================================
echo ABET CPE Course Mapping - Build Script
echo ==========================================
echo.

REM Check if pyinstaller is installed
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo Building executable...
echo.

set HOOK_DIR=pyinstaller_hooks

REM Build the executable
pyinstaller --clean --noconfirm ^
    --name "ABET-CPE-Mapper" ^
    --windowed ^
    --onedir ^
    --additional-hooks-dir "%HOOK_DIR%" ^
    --add-data "templates;templates" ^
    --add-data "static;static" ^
    --add-data "abet_organized.json;." ^
    --add-data "courses_organized.json;." ^
    --add-data "course_abet_mapping.json;." ^
    --hidden-import=webview ^
    --hidden-import=webview.platforms.winforms ^
    --hidden-import=werkzeug ^
    --hidden-import=flask ^
    app.py

if errorlevel 1 (
    echo.
    echo Build failed.
    exit /b 1
)

echo.
echo Build complete!
echo.
echo Executable location:
echo    dist\ABET-CPE-Mapper\
echo.
echo To distribute:
echo    1. Zip the entire 'dist\ABET-CPE-Mapper' folder
echo    2. Send to others
echo    3. Recipients extract and double-click 'ABET-CPE-Mapper.exe' to run
echo.
echo State file: course_abet_mapping.json will be created next to the executable
echo    after first run. This file contains all your mappings.
echo.

pause
