#!/bin/bash
# Build script for ABET CPE Course Mapping System
# Creates a standalone executable for the current platform

echo "=========================================="
echo "ABET CPE Course Mapping - Build Script"
echo "=========================================="
echo ""

# Check if pyinstaller is installed
if ! command -v pyinstaller &> /dev/null
then
    echo "❌ PyInstaller not found. Installing..."
    pip install pyinstaller
fi

echo "🔨 Building executable..."
echo ""

# Build the executable
pyinstaller --clean --noconfirm \
    --name "ABET-CPE-Mapper" \
    --windowed \
    --onedir \
    --add-data "templates:templates" \
    --add-data "static:static" \
    --add-data "abet_organized.json:." \
    --add-data "courses_organized.json:." \
    --add-data "course_abet_mapping.json:." \
    --hidden-import=webview \
    --hidden-import=webview.platforms.cocoa \
    --hidden-import=werkzeug \
    --hidden-import=flask \
    --osx-bundle-identifier=edu.uta.cpe.abet-mapper \
    app.py

echo ""
echo "✅ Build complete!"
echo ""
echo "📦 Executable location:"
echo "   dist/ABET-CPE-Mapper/"
echo ""
echo "📋 To distribute:"
echo "   1. Zip the entire 'dist/ABET-CPE-Mapper' folder"
echo "   2. Send to others"
echo "   3. Recipients extract and double-click 'ABET-CPE-Mapper' to run"
echo ""
echo "💾 State file: course_abet_mapping.json will be created next to the executable"
echo "   after first run. This file contains all your mappings."
echo ""
