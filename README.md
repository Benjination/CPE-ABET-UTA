# ABET CPE Course Mapping System

Web application for reviewing, mapping, and reporting ABET learning outcome coverage across Computer Engineering courses.

## What the Website Does

- Shows ABET outcomes organized by knowledge area
- Shows course descriptions and mapped outcomes
- Lets users map courses to ABET requirements
- Highlights coverage gaps when an outcome is not mapped to any course
- Saves shared edits to the hosted database so updates are visible to all users

## Main Interface

The site is organized into four main tabs:

- `Coverage Overview`
    Shows total courses, total ABET outcomes, mapped outcomes, and overall coverage percentage.

- `ABET Outcomes`
    Lets users browse and search ABET requirements by area, category, and subarea.

- `Courses`
    Lets users browse courses and inspect the ABET outcomes already mapped to each course.

- `Course Mapping`
    Lets users select a course and add or remove mapped ABET outcomes.

- `Coverage Gaps`
    Shows ABET outcomes that are not currently mapped to any course.

## How to Use It

### Review coverage

Start in `Coverage Overview` to see whether coverage is complete and which areas are weakest.

### Inspect ABET outcomes

Use `ABET Outcomes` to search requirements and review how outcomes are grouped.

### Inspect courses

Use `Courses` to open a course and review its mapped ABET coverage.

### Update mappings

Use `Course Mapping` to select a course and check or uncheck ABET outcomes.

- Checkbox edits in the mapping panel require clicking `Save Changes`.
- Removing an outcome with the red `x` inside a course detail view saves immediately after confirmation.
- Assigning a coverage gap to a course also saves immediately.

### Coverage gaps

If an outcome is not mapped to any course, it appears in `Coverage Gaps` and the overall percentage drops accordingly.

## Printing and Export

### Course print view

From a course detail view, users can print a course summary with its mapped ABET outcomes using `Print Course + ABET Outcomes`.

### Coverage matrix export

From `Coverage Overview`, users can export the full coverage matrix. The matrix lists ABET requirements as rows and courses as columns so coverage can be reviewed in spreadsheet form.

## Shared Saving Behavior

The hosted website uses PostgreSQL on Render for mapping persistence.

- When a user saves a change, it is stored centrally.
- Other users opening the site later from another computer or location will see the saved update.
- The site does not require users to manually pass around JSON files.

## Local Run

Local run is optional and mainly useful for development.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

App runs at `http://localhost:5001` by default.

## Deployment Notes

This repository is configured for Render using `render.yaml`.

- Mapping persistence is stored in PostgreSQL when `DATABASE_URL` is set.
- `abet_organized.json` and `courses_organized.json` remain source catalog files.
- If `DATABASE_URL` is not set, mapping falls back to local `course_abet_mapping.json`.

## Health/Mode Check

Use this endpoint to confirm which storage backend is active:

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
