from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

class FirewallRule(Base):
    __tablename__ = "firewall_rules"

    id = Column(Integer, primary_key=True, index=True)
    rule_name=Column(String, index=True)
    action=Column(String)

    def __repr__(self):
         return f"<FirewallRule(id={self.id}, rule_name={self.rule_name}, action={self.action})>"

    # cve_id = Column(String, index=True, nullable=False)  # Link to CVE that triggered the rule
    # rule_description = Column(String, nullable=False)  # Rule description, e.g., "DROP traffic from IPs with buffer overflow attempt"
    # created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for when the rule was created

    # def __repr__(self):
    #     return f"<FirewallRule(id={self.id}, cve_id={self.cve_id}, rule_description={self.rule_description})>"
