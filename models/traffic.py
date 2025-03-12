from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

class TrafficLog(Base):
    __tablename__ = "traffic_logs"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)
