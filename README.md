# Wine Starter Render Ready

Starter minimal avec :
- backend FastAPI
- frontend React + Vite
- configuration Render via `render.yaml`

## Structure

- `backend/` : API FastAPI
- `frontend/` : interface React
- `render.yaml` : déploiement automatique Render

## Lancement local

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Déploiement Render

1. Pousse ce projet sur GitHub
2. Dans Render, choisis **New +**
3. Sélectionne **Blueprint**
4. Choisis ce repo
5. Render lira automatiquement `render.yaml`
6. Ajoute la variable `SECRET_KEY` si tu veux autre chose que la valeur par défaut
7. Déploie

### URLs attendues
- Backend : `/docs`
- Frontend : service statique Render
