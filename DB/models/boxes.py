from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from DB import Base

class Box(Base):
    __tablename__ = "boxes"
    
    box_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    price_per_box = Column(Float, nullable=False)
    
    product = relationship("Product", backref="boxes")
    
    def __repr__(self):
        return f"<Box({self.box_id}, {self.product_id}, {self.quantity})>"