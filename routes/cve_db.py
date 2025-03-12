from fastapi import APIRouter

router = APIRouter()

# Simulating a simple CVE database with a few known vulnerabilities
known_cves = [
    {"cve_id": "CVE-2023-0001", "description": "Buffer Overflow Vulnerability"},
    {"cve_id": "CVE-2023-0002", "description": "SQL Injection Vulnerability"},
]

@router.post("/check_cve")
def check_cve(data: dict):
    """
    Simulate CVE detection by matching signatures.
    """
    signature = data.get("signature", "")
    matched_cves = [cve for cve in known_cves if cve["description"] in signature]
    
    if matched_cves:
        return {"status": "Malicious CVE signature detected", "matched_cves": matched_cves}
    
    return {"status": "No known CVEs detected"}
