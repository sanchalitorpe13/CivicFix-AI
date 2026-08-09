<<<<<<< HEAD
# CivicFix AI 🚀

**CivicFix AI** is an AI-powered community issue reporting and prioritization prototype for HackDevengers 1.0.

## Problem
Community complaints about potholes, streetlights, garbage, drainage and safety are often unstructured. That makes triage and routing slower.

## Solution
Users describe an issue in plain language. CivicFix AI turns it into a structured report containing category, urgency, summary, recommended action, department and tags.

## Stack
React + Vite · FastAPI · Python · Pydantic · Google Gemini API

## Flow
User → React → `POST /api/analyze` → FastAPI → Gemini → validated JSON → Result dashboard

If Gemini is unavailable, the backend uses a deterministic keyword-based fallback so the demo remains usable.

## Local setup
### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Put your Gemini API key in .env
uvicorn app.main:app --reload
```
Backend: `http://127.0.0.1:8000` · Swagger: `/docs`

### Frontend
```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```
Frontend: `http://localhost:5173`

## Deployment
Backend: Render Web Service, root `backend`, build `pip install -r requirements.txt`, start `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.

Frontend: Vercel, root `frontend`, build `npm run build`, output `dist`, environment variable `VITE_API_URL=https://YOUR-BACKEND.onrender.com`.

## Environment variables
Backend: `GEMINI_API_KEY`, `GEMINI_MODEL`, `FRONTEND_ORIGIN`
Frontend: `VITE_API_URL`

Never commit real API keys.

## Future scope
Map-based reporting, image issue detection, duplicate complaint detection, multilingual support, citizen history, department dashboards and analytics.

## Safety
This is a prototype routing/classification aid. AI output should be reviewed by responsible authorities before operational decisions.
=======
# CivicFix-AI
CivicFix AI transforms unstructured community complaints into prioritized, actionable civic reports using AI.
>>>>>>> 93ac7036a351aeb7ebb4b5f5f60360423a2366dc
