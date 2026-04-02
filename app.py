#!/usr/bin/env python3
"""
ABET CPE Course Mapping Desktop Application
Native desktop app for managing course-to-ABET learning outcome mappings
"""

from flask import Flask, render_template, jsonify, request
import json
import os
import sys
import threading
import webview

# Get the base path for resources (works with PyInstaller)
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Get the directory where the executable/script is located (for writable files)
def get_data_dir():
    """Get directory for writable data files"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return os.path.dirname(sys.executable)
    else:
        # Running as script
        return os.path.abspath(".")

app = Flask(__name__, 
            template_folder=get_resource_path('templates'),
            static_folder=get_resource_path('static'))

# Disable Flask debug output for cleaner desktop app experience
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Load data
def load_data():
    data_dir = get_data_dir()
    
    with open(get_resource_path('abet_organized.json'), 'r') as f:
        abet_data = json.load(f)
    
    with open(get_resource_path('courses_organized.json'), 'r') as f:
        courses_data = json.load(f)
    
    # Mapping file is writable, so look in data directory
    mapping_path = os.path.join(data_dir, 'course_abet_mapping.json')
    
    # If mapping file doesn't exist in data dir, copy from resources
    if not os.path.exists(mapping_path):
        import shutil
        shutil.copy(get_resource_path('course_abet_mapping.json'), mapping_path)
    
    with open(mapping_path, 'r') as f:
        mapping_data = json.load(f)
    
    return abet_data, courses_data, mapping_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/abet')
def get_abet():
    """Get all ABET learning outcomes"""
    abet_data, _, _ = load_data()
    return jsonify(abet_data)

@app.route('/api/courses')
def get_courses():
    """Get all courses"""
    _, courses_data, _ = load_data()
    return jsonify(courses_data)

@app.route('/api/mapping')
def get_mapping():
    """Get course-ABET mappings"""
    _, _, mapping_data = load_data()
    return jsonify(mapping_data)

@app.route('/api/stats')
def get_stats():
    """Get statistics about coverage"""
    abet_data, courses_data, mapping_data = load_data()
    
    # Count total outcomes
    total_outcomes = 0
    outcomes_by_area = {}
    
    for area_code, area_info in abet_data.items():
        count = 0
        for category, subareas in area_info['categories'].items():
            for subarea, outcomes in subareas.items():
                count += len(outcomes)
        total_outcomes += count
        outcomes_by_area[area_code] = {
            'name': area_info['name'],
            'count': count
        }
    
    # Count mapped vs unmapped
    mapped_outcomes = set(mapping_data.get('abet_to_course', {}).keys())
    
    stats = {
        'total_courses': len(courses_data),
        'total_outcomes': total_outcomes,
        'mapped_outcomes': len(mapped_outcomes),
        'unmapped_outcomes': total_outcomes - len(mapped_outcomes),
        'coverage_percentage': (len(mapped_outcomes) / total_outcomes * 100) if total_outcomes > 0 else 0,
        'outcomes_by_area': outcomes_by_area
    }
    
    return jsonify(stats)

@app.route('/api/mapping/save', methods=['POST'])
def save_mapping_route():
    """Save course-ABET mappings"""
    new_mapping = request.json
    
    data_dir = get_data_dir()
    mapping_path = os.path.join(data_dir, 'course_abet_mapping.json')
    
    with open(mapping_path, 'w') as f:
        json.dump(new_mapping, f, indent=2)
    
    return jsonify({'success': True})

@app.route('/api/remove-mapping', methods=['POST'])
def remove_mapping():
    """Remove an outcome from a course"""
    data = request.json
    outcome_id = data.get('outcome_id')
    course_code = data.get('course_code')
    
    if not outcome_id or not course_code:
        return jsonify({'error': 'Missing outcome_id or course_code'}), 400
    
    _, _, mapping_data = load_data()
    
    # Remove from course_to_abet
    if course_code in mapping_data['course_to_abet']:
        if outcome_id in mapping_data['course_to_abet'][course_code]:
            mapping_data['course_to_abet'][course_code].remove(outcome_id)
    
    # Remove from abet_to_course
    if outcome_id in mapping_data['abet_to_course']:
        if course_code in mapping_data['abet_to_course'][outcome_id]:
            mapping_data['abet_to_course'][outcome_id].remove(course_code)
            # Clean up if no courses left
            if not mapping_data['abet_to_course'][outcome_id]:
                del mapping_data['abet_to_course'][outcome_id]
    
    # Save the updated mapping
    data_dir = get_data_dir()
    mapping_path = os.path.join(data_dir, 'course_abet_mapping.json')
    with open(mapping_path, 'w') as f:
        json.dump(mapping_data, f, indent=2)
    
    return jsonify({'success': True})

@app.route('/api/gaps')
def get_gaps():
    """Find ABET outcomes not covered by any course"""
    abet_data, _, mapping_data = load_data()
    
    # Get all mapped outcome IDs
    mapped_outcome_ids = set(mapping_data.get('abet_to_course', {}).keys())
    
    # Find unmapped outcomes
    gaps = []
    for area_code, area_info in abet_data.items():
        for category, subareas in area_info['categories'].items():
            for subarea, outcomes in subareas.items():
                for outcome in outcomes:
                    outcome_id = f"{area_code}.{category}.{subarea}.{outcome['id']}"
                    if outcome_id not in mapped_outcome_ids:
                        gaps.append({
                            'area_code': area_code,
                            'area_name': area_info['name'],
                            'category': category,
                            'subarea': subarea,
                            'id': outcome['id'],
                            'outcome': outcome['outcome'],
                            'full_id': outcome_id
                        })
    
    return jsonify(gaps)

def start_flask():
    """Start Flask server in a separate thread"""
    app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("ABET CPE Course Mapping System")
    print("="*60)
    print("\n🚀 Starting desktop application...")
    print("="*60 + "\n")
    
    # Start Flask in background thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    
    # Wait a moment for Flask to start
    import time
    time.sleep(1.5)
    
    # Create desktop window
    window = webview.create_window(
        title='ABET CPE Course Mapping',
        url='http://127.0.0.1:5001',
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
        min_size=(1200, 800)
    )
    
    # Start the GUI (blocking call)
    webview.start()
