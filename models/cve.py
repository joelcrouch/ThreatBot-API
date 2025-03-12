#for cve db table

from database import Base
from sqlalchemy import Column, Integer, String

class CVE(Base):
    __tablename__="cves"

    id=Column(Integer, primary_key=True, index=True)
    cve_id=Column(String, unique=True, nullable=False)
    description=Column(String, nullable=False)

    