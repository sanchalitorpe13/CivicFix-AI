def fallback_analysis(text: str) -> dict:
    t = text.lower()
    rules = [
        (["fire", "smoke", "explosion"], "Fire/Safety", "Critical", "Fire and Safety Department", ["fire", "safety"]),
        (["pothole", "road"], "Road Infrastructure", "Medium", "Municipal Roads Department", ["road", "infrastructure"]),
        (["garbage", "waste", "trash", "dump"], "Waste Management", "Medium", "Municipal Waste Department", ["waste", "cleanliness"]),
        (["streetlight", "street light", "lamp"], "Streetlight", "High", "Municipal Electrical Department", ["streetlight", "safety"]),
        (["water leak", "leakage", "drain", "sewage"], "Water & Drainage", "High", "Water & Drainage Department", ["water", "drainage"]),
        (["accident", "injury", "dangerous", "exposed wire"], "Public Safety", "High", "Public Safety Department", ["safety", "hazard"]),
    ]
    for keys, category, urgency, dept, tags in rules:
        if any(k in t for k in keys):
            return {"category": category, "urgency": urgency, "summary": text[:220], "recommended_action": f"Inspect the reported {category.lower()} issue and assign it to the appropriate field team.", "department": dept, "tags": tags, "ai_generated": False}
    return {"category": "General Community Issue", "urgency": "Medium", "summary": text[:220], "recommended_action": "Review the report, verify the issue, and route it to the appropriate department.", "department": "Civic Administration", "tags": ["community", "report"], "ai_generated": False}
