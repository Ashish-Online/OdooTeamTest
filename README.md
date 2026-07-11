# Backend skeleton (FastAPI + MySQL)
# Ashish

## Setup
1. Start MySQL from XAMPP control panel, create a database (e.g. `hackathon_db`) in phpMyAdmin.
2. `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. `pip install -r requirements.txt`
4. `cp .env.example .env` and fill in real values.
5. `uvicorn app.main:app --reload`
6. Open http://localhost:8000/docs to test every endpoint without needing the frontend yet.

## What's already wired up
- Password hashing (bcrypt) - never stores plain-text passwords
- JWT login (`/auth/register`, `/auth/login`) - protects routes with `Depends(get_current_user)`
- CORS configured for your React dev server
- Input validation via Pydantic (invalid email, missing fields, etc. auto-rejected)
- MySQL via SQLAlchemy - swap `items.py`/`item.py` for your real problem-statement entities

## Folder map
```
app/
  main.py          entrypoint, CORS, routers
  core/config.py   reads .env
  core/security.py password hashing + JWT
  db/session.py    DB engine + get_db dependency
  models/          SQLAlchemy tables
  schemas/         Pydantic request/response shapes
  routers/         one file per resource (auth, items, ...)
  dependencies.py  get_current_user - reuse this to protect any route
```
