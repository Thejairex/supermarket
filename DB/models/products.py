from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from DB import Base

class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product = Column(String(150), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    cost_unit = Column(Float, nullable=False)
    inflation_rate = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    
    category = relationship("Category", backref="products")
    
    def __repr__(self):
        return f"<Product({self.product_id}, {self.product}, {self.price}, {self.category_id})>"