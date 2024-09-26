from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DB:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///database.db")
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def add(self, model):
        self.session.add(model)
        self.commit()
        
    def get_all(self, model):
        return self.session.query(model).all()
    
        
    def get_by_column(self, model, column, value):
        return self.session.query(model).filter(getattr(model, column) == value).first()
        
    def get_last_record(self, model):
        return self.session.query(model).order_by(model.product_id.desc()).first()
        
        
    def commit(self):
        self.session.commit()
        
    def close(self):
        self.session.close()