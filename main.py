# from db import DB
from DB import DB
from DB.models import Category, Product, Box


class Store:
    def __init__(self):
        self.db = DB()
        self.db.create_tables()

    def add_product(self):
        categories = self.db.get_all(Category)
        if len(categories) != 0:
            print("lista de categorias: ", categories)
            product = input("Ingrese producto: ")
            category = int(input("Ingrese id de categoria: "))
            cost_unit = float(input("Ingrese costo unitario: "))
            inflation_rate = float(input("Ingrese tasa de inflacion : "))
            quantity = int(input("Ingrese cantidad de unidades por caja: "))
            price = round(round((cost_unit * ( 1 + inflation_rate / 100)), 2) * 1.4, 1)
            
            print("El precio es: ", price)
            
            self.db.add(
                Product(
                    product=product,
                    category_id=category,
                    cost_unit=cost_unit,
                    inflation_rate=inflation_rate,
                    price=price))
            
            self.db.add(
                Box(
                    product_id = self.db.get_last_record(Product).product_id,
                    quantity = quantity,
                    price_per_box = (cost_unit * quantity),
                )
            )
            
        else:
            print("No hay categorias. Por favor agregue una categoria")
            
    def add_category(self):
        print("Agregando categoria")
        print("lista de categorias: ", self.db.get_all(Category))
        print()
        self.db.add(Category(category=input("Ingrese categoria: ")))
        


def main():
    store = Store()
    print("Backend de supermarket")
    print("1. Agregar producto")
    print("2. Agregar categoria")
    print("3. Exit")
    try:
        option = int(input("Choose an option: "))

    except ValueError:
        print("Invalid option")
    # option = int(input("Choose an option: "))

    if option == 1:
        store.add_product()
    elif option == 2:
        store.add_category()
        
    elif option == 3:
        pass


if __name__ == "__main__":

    main()
