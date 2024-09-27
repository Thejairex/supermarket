from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class DB:
    def __init__(self) -> None:
        """
        Engine and Session initialization
        
        """
        self.engine = create_engine("sqlite:///database.db")
        self.session = sessionmaker(bind=self.engine)
        self.session = self.session()

    def create_tables(self):
        """
        Creates the tables in the database if they don't exist.
        
        returns: None
        """
        Base.metadata.create_all(self.engine)

    def add(self, model):
        """
        Adds a model object to the database and commits the changes.
        
        args:
            model: The model object to be added to the database (Base).
            
        returns: None
        """
        self.session.add(model)
        self.commit()
        
    def __order_by(self, query, order_by, order):
        """
        Private method for ordering the query
        
        args:
            query: The query to be ordered.
            order_by: The column name to be used for ordering.
            order: The order to be used for ordering (optional, default is "asc").
            
        returns: The ordered query.
        """
        if order == "asc":
            return query.order_by(getattr(query, order_by))

        elif order == "desc":
            return query.order_by(getattr(query, order_by).desc())

    def get_all(self, model, order_by: str = None, order="asc"):
        """
        Gets all the model objects from the database.
        
        args:
            model: The model object to be added to the database (Base).
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "asc").
            
        returns: A list of model objects.
        """
        query = self.session.query(model)
        
        if order_by:
            query = self.__order_by(query, order_by, order)
            
        return query.all()

    def get_where(self, model, column, value, order_by: str = None, order="desc"):
        """
        Gets all the model objects from the database that match the given column and value.
        
        args:
            model: The model object to be added to the database (Base).
            column: The column name to be used for filtering.
            value: The value to be used for filtering.
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "desc").
        
        returns: A list of model objects that match the given column and value.
        """
        query = self.session.query(model).filter(getattr(model, column) == value)
        
        if order_by:
            query = self.__order_by(query, order_by, order)
        
        return query.all()

    def get_record(self, model, column, value):
        return self.session.query(model).filter(getattr(model, column) == value).first()
    
    def get_last_record(self, model):
        return self.session.query(model).order_by(model.model_id.desc()).first()

    def get_where_record(self, model, column, value, order_by=None, order="desc"):
        """
        Gets the first model object from the database that matches the given column and value.
        
        args:
            model: The model object to be added to the database (Base).
            column: The column name to be used for filtering.
            value: The value to be used for filtering.
            order_by: The column name to be used for ordering (optional).
            order: The order to be used for ordering (optional, default is "desc").
        
        returns: The first model object that matches the given column and value.
        """
        
        query = self.session.query(model).filter(getattr(model, column) == value)
        
        if order_by:
            query = self.__order_by(query, order_by, order)
        
        return query.first()



    def delete_record(self, model, column, value):
        self.session.query(model).filter(
            getattr(model, column) == value).delete()

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()
