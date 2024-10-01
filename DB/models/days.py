from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from DB import Base


class Days(Base):
    __tablename__ = "days"

    day_id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(String(150), unique=False, nullable=False)
    money_start = Column(Float, nullable=False)
    money_end = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship("User", backref="days")

    __table_args__ = (
        UniqueConstraint('day', 'user_id', name='_user_day_uc'),
    )

    def __repr__(self):
        return f"<Day({self.day_id}, {self.day}, {self.money_start}, {self.money_end})>"
