def classify(text: str, source: str) -> dict[str, str]:
    if not text.strip() or not source.strip():
        return {"queue": "REVIEW", "decision": "BLOCK"}
    queue = "IT" if "password" in text.lower() else "GENERAL"
    return {"queue": queue, "decision": "PASS"}