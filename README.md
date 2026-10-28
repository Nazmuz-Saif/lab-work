# Lab Project (base)

Django + DRF backend, React (Vite + Tailwind) frontend. One blank page, ready for the lab task.

## Run
Backend:
    cd backend
    python -m venv venv && venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Frontend (another terminal):
    cd frontend
    npm install
    npm run dev          # http://localhost:5173

## Tests
    cd backend
    python manage.py test                              # unit tests
    python -m unittest ui_tests.ui_smoke -v    # UI test (both servers up, Chrome needed)
