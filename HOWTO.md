### test cve_db idea

curl -X POST "http://127.0.0.1:8000/api/detection/detect_threat" -H "Content-Type: application/json" -d '{"threat_type": "buffer_overflow"}'

should be:{
"status": "Malicious CVE signature detected",
"matched_cves": [
{
"cve_id": "CVE-2023-0001",
"description": "Buffer Overflow Vulnerability"
}
]
}

this is a c/p from terminal:
eg: ~/fastAPITester$ curl -X POST "http://127.0.0.1:8000/api/cve/check_cve" -H "Content-Type: application/json" -d '{"signature": "Buffer Overflow Vulnerability"}'

{"status":"Malicious CVE signature detected","matched_cves":[{"cve_id":"CVE-2023-0001","description":"Buffer Overflow Vulnerability"}]}

works

### test firewall generation idea

curl -X POST "http://127.0.0.1:8000/api/firewall/generate_rule" -H "Content-Type: application/json" -d '{"cve_id": "CVE-2023-0001"}'

in action: ~/fastAPITester$ curl -X POST "http://127.0.0.1:8000/api/firewall/generate_rule" -H "Content-Type: application/json" -d '{"cve_id": "CVE-2023-0001"}'
{"rule":"DROP traffic form IPs wiht buffer overflow attempt."}(tester)

great.

### test detection
