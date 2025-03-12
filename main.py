
from fastapi import FastAPI
from routes import test, traffic, cve_db, firewall
app=FastAPI(title="Minimal APP")

app.include_router(test.router, prefix="/api")
app.include_router(traffic.router, prefix="/api/traffic")
app.include_router(cve_db.router, prefix="/api/cve")
app.include_router(firewall.router, prefix="/api/firewall")

@app.get("/")
def home():
    return {"message":"Api is running!"}
