from database import engine, Base, SessionLocal
from fastapi import FastAPI, Depends
from routes import test, traffic, cve_db, firewall, detection
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from models import FirewallRule, CVE

#from models import firewall
#from models import FireWallRule

# def create_tables_if_not_exist():
#     inspector=inspect(engine)
#     if not inspector.has_table("cves"):
#         Base.metadata.create_all(bind=engine)("postgesql://new_user:newpassword@localhost/cve_db")

# create_tables_if_not_exist()


# # Test the database connection by creating a test route
# @app.get("/test-db")
# def test_db():
#     try:
#         # Try to create a session and perform a simple query
#         db = SessionLocal()
#         result = db.execute("SELECT 1")  # Simple SQL query to check connection
#         db.close()
#         return {"message": "Database connection successful!", "result": result.fetchall()}
#     except Exception as e:
#         return {"error": str(e)}

# # Test firewall rule insertion and query
# @app.get("/test-firewall-rule")
# def test_firewall_rule():
#     try:
#         db = SessionLocal()

#         # Insert a test firewall rule into the database
#         test_rule = firewall.FirewallRule(
#             cve_id="CVE-2023-0001", 
#             rule_description="DROP traffic from IPs with buffer overflow attempt"
#         )
#         db.add(test_rule)
#         db.commit()
#         db.refresh(test_rule)
        
#         # Query the inserted firewall rule
#         db_rule = db.query(firewall.FirewallRule).filter(firewall.FirewallRule.id == test_rule.id).first()
#         db.close()
        
#         return {"message": "Test firewall rule inserted", "rule": db_rule}
#     except Exception as e:
#         return {"error": str(e)}
    
app=FastAPI(title="Minimal APP")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(test.router, prefix="/api")
app.include_router(traffic.router, prefix="/api/traffic")
app.include_router(cve_db.router, prefix="/api/cve")
app.include_router(firewall.router, prefix="/api/firewall")
app.include_router(detection.router, prefix="/api/detection")

@app.get("/")
def home():
    return {"message":"Api is running!"}
