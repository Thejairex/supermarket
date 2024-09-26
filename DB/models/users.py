from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from DB import Base

class User(UserMixin,Base):
    __tablename__ = "users"
    user_id  = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    role = Column(String(150), nullable=False, default="user")

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f"<User({self.user_id}, {self.username}, {self.password}, {self.role})>"