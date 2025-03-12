from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze_traffic(data: dict):
    """
    Simulate basic traffic analysis based on source IP.
    """
    source_ip = data.get("source_ip", "unknown")
    if source_ip == "192.168.1.1":
        return {"status": "Malicious traffic detected from IP: 192.168.1.1"}
    return {"status": f"Traffic from {source_ip} is safe."}
