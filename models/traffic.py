from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class TrafficLog(Base):
    __tablename__ = "traffic_logs"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String, nullable=False)
    destination_ip = Column(String, nullable=False)
    protocol = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    firewall_rule_id = Column(Integer, ForeignKey("firewall_rules.id"))

    firewall_rule = relationship("FirewallRule", back_populates="traffic_logs")

    def __repr__(self):
        return f"<TrafficLog(id={self.id}, source_ip={self.source_ip},destination_ip={self.destination_ip}, protocol={self.protocol},timestamp={self.timestamp})>"