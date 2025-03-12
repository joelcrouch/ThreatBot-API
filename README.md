# AI-Powered CVE detection API gateway

This project is an AI-powered API gateway designed to detect and analyze network traffic based on known CVEs (Common Vulnerabilities and Exposures). It features multiple modules including traffic analysis, CVE detection, firewall rule generation, and more.

## Project Structure

- **FastAPI Framework**: Used to build the API endpoints.
- **Traffic Module**: Analyzes incoming traffic and flags malicious traffic based on predefined signatures.
- **CVE Database Module**: Checks the provided signature against known CVEs and returns matching vulnerabilities.
- **Firewall Rule Module**: Generates firewall rules based on detected CVEs to mitigate potential threats.
- **Detection Module**: Further analyzes threats and proposes mitigations.

## API Endpoints

1. **Traffic Analysis**

   - **URL**: `/api/traffic/analyze`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "source_ip": "192.168.1.1"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "Malicious traffic detected from IP: 192.168.1.1"
     }
     ```

2. **CVE Detection**

   - **URL**: `/api/cve/check_cve`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "signature": "Buffer Overflow Vulnerability"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "Malicious CVE signature detected",
       "matched_cves": [
         {
           "cve_id": "CVE-2023-0001",
           "description": "Buffer Overflow Vulnerability"
         }
       ]
     }
     ```

3. **Firewall Rule Generation**
   - **URL**: `/api/firewall/generate_rule`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "cve_id": "CVE-2023-0001"
     }
     ```
   - **Response**:
     ```json
     {
       "rule": "DROP traffic from IPs with buffer overflow attempt."
     }
     ```

## Installation

TODO

Probalbly, clone,setup environment,start the server,test the endpoints,

## Project Future Directions

- **Enhanced Traffic Analysis:** Integrate AI/ML-based detection for more advanced traffic analysis.
- **Dynamic CVE Database:** Integrate with an external source for real-time CVE updates.
- **Automated Firewall Rule Creation:** Extend the firewall module to handle different types of attacks and propose mitigation rules dynamically.

## Contributions

ABSOLUTELY welcome to contributions. I welcome any and all advice, hearsay, comments. I love to find mistakes and learn from them.
