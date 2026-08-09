import json, os
from google import genai
from google.genai import types

PROMPT = """You are CivicFix AI, a community issue structuring assistant. Return ONLY JSON with keys: category, urgency, summary, recommended_action, department, tags. urgency must be Low, Medium, High, or Critical. Use practical categories such as Road Infrastructure, Streetlight, Waste Management, Water & Drainage, Public Safety, Fire/Safety, Public Transport, Environment, General Community Issue. Do not invent addresses, phone numbers, laws, or officials. Keep summary under 30 words and recommended_action under 35 words. tags: 2-5 short strings. This is a prototype routing aid, not an official decision."""

def analyze_with_gemini(complaint: str) -> dict:
    key = os.getenv("GEMINI_API_KEY")
    if not key: raise RuntimeError("GEMINI_API_KEY missing")
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=f"{PROMPT}\n\nComplaint:\n{complaint}",
        config=types.GenerateContentConfig(temperature=0.2, response_mime_type="application/json")
    )
    data = json.loads(response.text)
    if data.get("urgency") not in {"Low", "Medium", "High", "Critical"}: data["urgency"] = "Medium"
    data["ai_generated"] = True
    return data
