import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import AnalyzeRequest, AnalysisResult
from .ai_service import analyze_with_gemini
from .fallback import fallback_analysis

load_dotenv()
app = FastAPI(title="CivicFix AI API", version="1.0.0")
origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
app.add_middleware(CORSMiddleware, allow_origins=[origin, "http://localhost:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root(): return {"name": "CivicFix AI", "status": "running"}

@app.get("/health")
def health(): return {"status": "healthy"}

@app.post("/api/analyze", response_model=AnalysisResult)
def analyze(req: AnalyzeRequest):
    text = req.complaint.strip()
    if len(text) < 10: raise HTTPException(400, "Please describe the issue in at least 10 characters.")
    try: result = analyze_with_gemini(text)
    except Exception: result = fallback_analysis(text)
    return result
