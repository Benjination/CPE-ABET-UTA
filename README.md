# ABET CPE Course Mapping System

Web application for managing and analyzing ABET learning outcome coverage across Computer Engineering courses.

## Features

- View ABET outcomes organized by knowledge area
- View courses and descriptions
- Interactive course-to-outcome mapping
- Coverage and gap analysis
- Shared persistence through PostgreSQL on Render

## Deployment

This repository is configured for Render web deployment using `render.yaml`.

### Required Render setup

1. Create a Render PostgreSQL service.
2. Create a Render web service connected to this repository.
3. Set environment variable `DATABASE_URL` on the web service using the database connection string.

## Local Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

App runs at `http://localhost:5001` by default.

## Persistence Model

- `course_outcome_mappings` are stored in PostgreSQL when `DATABASE_URL` is set.
- `abet_organized.json` and `courses_organized.json` remain source catalog files.
- If `DATABASE_URL` is not set, mapping falls back to local `course_abet_mapping.json`.

## Health/Mode Check

Use this endpoint to confirm storage backend:

`/api/storage-mode`

Expected for production:

- `backend: "database"`
- `database_connected: true`

## Project Structure

```
ABET CPE/
├── app.py
├── render.yaml
├── requirements.txt
├── abet_organized.json
├── courses_organized.json
├── course_abet_mapping.json
├── templates/
│   └── index.html
└── static/
    └── images/
        └── uta_logo_resized.png
```
