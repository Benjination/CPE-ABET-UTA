# Quick Start Guide

## For Users (Just Want to Run It)

### Option 1: Use the Executable (Recommended)
1. Ask the maintainer for the built version
2. Extract the `ABET-CPE-Mapper` folder
3. Double-click the executable
4. Wait for browser to open automatically

### Option 2: Run from Source
```bash
pip install -r requirements.txt
python app.py
```

## For Developers (Building Executables)

### Mac/Linux
```bash
./build.sh
```

### Windows
```cmd
build.bat
```

### Build Windows From macOS (GitHub Actions)
1. Push your latest changes to `main`
2. Open Actions in GitHub
3. Run `Build Windows Package`
4. Download artifact `ABET-CPE-Mapper-windows`
5. Send the downloaded zip to Steve

## Sharing Your Mappings

1. Make your changes in the app
2. Copy the entire application folder (includes `course_abet_mapping.json`)
3. Send to colleague
4. They extract and run - they'll see your mappings
5. If they make changes, their version diverges from yours

## Important Files

- `course_abet_mapping.json` - Your mapping data (this is what you send to share state)
- `abet_organized.json` - ABET requirements (shouldn't change)
- `courses_organized.json` - Course info (shouldn't change)
- `app.py` - The application code

## Platforms

✅ macOS (Intel & Apple Silicon)
✅ Windows (10/11)
✅ Linux (Ubuntu, Fedora, etc.)

Build on the target platform you want to distribute for.
