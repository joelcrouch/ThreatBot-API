from fastapi import APIRouter

router = APIRouter()

@router.post("/detect_threat")
def detect_threat(data: dict):
    """
    Simulate threat detection by analyzing traffic.
    """
    threat_type = data.get("threat_type", "")
    if threat_type == "buffer_overflow":
        return {"status": "Threat detected: Buffer Overflow"}
    elif threat_type == "sql_injection":
        return {"status": "Threat detected: SQL Injection"}
    return {"status": "No threat detected"}
