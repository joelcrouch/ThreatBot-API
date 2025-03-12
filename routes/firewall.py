from fastapi import APIRouter

router=APIRouter()

@router.post("/generate_rule")
def generate_firewall_rule(data: dict):
    #simulate generationg firewall rules based on CVE detection or traffic 
    #analsis

    cve_id=data.get("cve_id")
    if cve_id=="CVE-2023-0001":
        return {"rule":"DROP traffic form IPs wiht buffer overflow attempt."}
    elif cve_id=="CVE-2023-0002":
        return {"rule": "BLOCK SQL injection payload in HTTP requests."}
    return {"rule":"Allow rule(no rule generated)"}