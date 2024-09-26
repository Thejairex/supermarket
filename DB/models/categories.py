from sqlalchemy import Column, Integer, String
from DB import Base

class Category(Base):
    __tablename__ = "categories"
    
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(150), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<Category({self.category_id}, {self.category})>"