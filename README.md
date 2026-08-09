# 🏙️ CivicFix AI

> **AI-powered civic issue analysis and routing for faster community action.**

CivicFix AI is a web-based AI prototype that transforms citizen complaints written in natural language into structured, actionable reports.

Instead of requiring users to know which department should handle a problem, CivicFix AI analyzes a complaint, identifies the issue category, estimates urgency, generates a concise summary, recommends an action, suggests the responsible department, and extracts relevant tags.

Built for **HackDevengers 1.0**.

---

## 🚀 Demo

> Add your deployed frontend URL here after deployment.

**Live Demo:** `YOUR_DEPLOYED_URL`

---

## 🎯 Problem

Citizens frequently report problems such as:

- Potholes and damaged roads
- Broken streetlights
- Garbage accumulation
- Water leakage
- Public infrastructure damage
- Other local civic issues

However, complaints are often unstructured and may not contain enough information for quick routing.

This can result in:

- Incorrect department assignment
- Delayed response
- Difficulty prioritizing urgent issues
- Repetitive manual classification
- Poorly structured complaint data

---

## 💡 Our Solution

CivicFix AI acts as an intelligent first layer between a citizen and a civic response system.

A user simply describes an issue in plain language.

For example:

> "There is a large pothole near the main bus stop causing traffic problems."

CivicFix AI converts it into a structured report:

```json
{
  "category": "Road Infrastructure",
  "urgency": "Medium",
  "summary": "There is a large pothole near the main bus stop causing traffic problems.",
  "recommended_action": "Inspect the reported road infrastructure issue and assign it to the appropriate field team.",
  "department": "Municipal Roads Department",
  "tags": [
    "road",
    "infrastructure"
  ],
  "ai_generated": true
}
