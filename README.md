# ABET CPE Course Mapping System

A desktop application for managing and analyzing ABET learning outcome coverage across Computer Engineering courses.

## 🎯 Features

- **View ABET Outcomes**: Browse all 934 ABET CPE learning outcomes organized by knowledge area
- **View Courses**: See all 22 courses with descriptions and learning outcomes
- **Interactive Mapping**: Map courses to ABET outcomes with checkbox interface
- **Coverage Analysis**: Real-time statistics showing mapping progress
- **Gap Analysis**: Identify unmapped ABET outcomes and assign them to courses
- **State Persistence**: All mappings are saved and persist between sessions

## 📦 Distribution Instructions

### For Users (Running the App)

#### Option 1: Double-Click Executable (Easiest)
1. Extract the `ABET-CPE-Mapper` folder
2. Double-click `ABET-CPE-Mapper` (Mac/Linux) or `ABET-CPE-Mapper.exe` (Windows)
3. Your browser will open automatically to http://localhost:5001
4. To stop: Close the terminal window or press Ctrl+C

#### Option 2: Run from Python (If you have Python installed)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 💾 State Management

**Your mappings are saved in:** `course_abet_mapping.json`

This file is automatically created next to the executable after first run. It contains all your course-to-ABET mappings.

**Sharing Your Work:**
- To send your mappings to someone: Include the `course_abet_mapping.json` file with the application
- To start fresh: Delete `course_abet_mapping.json` (it will be recreated with defaults)
- Each person can maintain their own version of the mappings

**Version Control:**
- Everyone starts with the same baseline mappings
- After making changes, each person has their own independent version
- To sync: Copy someone's `course_abet_mapping.json` file to replace yours

## 🔨 Building from Source

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Mac/Linux Build

```bash
# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Run build script
chmod +x build.sh
./build.sh
```

The executable will be created in `dist/ABET-CPE-Mapper/`

### Windows Build

```cmd
REM Install dependencies
pip install -r requirements.txt
pip install pyinstaller

REM Run build script
build.bat
```

The executable will be created in `dist\ABET-CPE-Mapper\`

### Distribution Package

After building, zip the entire `dist/ABET-CPE-Mapper` folder. This package contains:
- The executable
- All dependencies
- Templates and static files
- Default ABET and course data
- Initial mapping state

Recipients can simply extract and run - no installation needed!

## 📂 Project Structure

```
ABET CPE/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── build.sh                    # Build script (Mac/Linux)
├── build.bat                   # Build script (Windows)
├── abet_organized.json         # ABET outcomes data (read-only)
├── courses_organized.json      # Course data (read-only)
├── course_abet_mapping.json    # Mapping state (writable)
├── templates/
│   └── index.html             # Web interface
└── static/
    └── images/
        └── uta_logo_resized.png
```

## 🛠️ Technical Details

- **Framework**: Flask 3.1.3 (Python web framework)
- **Packaging**: PyInstaller (creates standalone executables)
- **Interface**: HTML/CSS/JavaScript (responsive web UI)
- **Data Format**: JSON (human-readable, easy to edit/version)
- **Platforms**: macOS, Windows, Linux

## 🎨 UTA Branding

The application features University of Texas at Arlington branding:
- Navy Blue (#005696) header
- Burnt Orange (#FF8200) accents
- UTA logo in header

## 📊 Data Statistics

- **ABET Knowledge Areas**: 12 areas (Circuits, Architecture, Logic, etc.)
- **Total ABET Outcomes**: 934 learning outcomes
- **Courses**: 22 CPE courses
- **Initial Coverage**: 638 outcomes mapped (68.3%)

## 🔄 Workflow

1. **Review Coverage**: Start with Coverage Overview tab to see current statistics
2. **Map by Course**: Use Course Mapping tab to review each course and check ABET outcomes
3. **Fill Gaps**: Use Coverage Gaps tab to find unmapped outcomes and assign to courses
4. **Analyze**: Return to Coverage Overview to see updated statistics
5. **Share**: Send the entire application folder (including `course_abet_mapping.json`) to colleagues

## ⚠️ Troubleshooting

### Port Already in Use
If you see "Address already in use", another instance is running:
- **Mac/Linux**: `lsof -ti:5001 | xargs kill -9`
- **Windows**: Open Task Manager and end `ABET-CPE-Mapper.exe`

### Browser Doesn't Open
Manually navigate to: http://localhost:5001

### Changes Not Saving
- Check that `course_abet_mapping.json` is writable
- Ensure you're clicking the "Save Changes" button in Course Mapping tab
- Gap assignments save automatically

### Build Fails
- Ensure Python 3.8+ is installed
- Update pip: `pip install --upgrade pip`
- Update PyInstaller: `pip install --upgrade pyinstaller`

## 📝 License

Internal tool for UTA Computer Engineering department use.

## 🤝 Support

For questions or issues, contact the Computer Engineering department.
