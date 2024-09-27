from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlalchemy
from DB import DB
from DB.models import Product, Category, Box

products_bp = Blueprint('products', __name__)
db = DB()

@products_bp.route('/', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        category_id = request.form['category_id']
        order_by = request.form['order_by']
        
        if category_id and category_id != 'All':
            products = db.get_where(Product, 'category_id', category_id, order_by=order_by)
            
        else:
            products = db.get_all(Product, order_by=order_by)
        
        categories = db.get_all(Category)
        return render_template('products.html', products=products,categories=categories)        
    
    products = db.get_all(Product)
    categories = db.get_all(Category)
    return render_template('products.html', products=products,categories=categories)

@products_bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product        = str(request.form['product'])
        category_id    = int(request.form['category_id'])
        stand          = str(request.form['stand'])
        cost_unit      = float(request.form['cost_unit'])
        inflation_rate = float(request.form['inflation_rate'])
        quantity       = int(request.form['quantity'])
        
        price = round(round((cost_unit * ( 1 + inflation_rate / 100)), 2) * 1.4, 1)
        
        product = Product(
            product        = product,
            category_id    = category_id,
            stand          = stand,
            cost_unit      = cost_unit,
            inflation_rate = inflation_rate,
            price          = price
        )
        try:
            db.add(product)
        except sqlalchemy.exc.IntegrityError as e:
            e = str(e)
            if 'UNIQUE constraint failed: products.product' in e:
                flash('El producto ya existe', 'error')
            else:
                flash('Error al agregar producto', 'error')
        
        try:
            box = Box(
                product_id = db.get_last_record(Product).product_id,
                quantity = quantity,
                price_per_box = (request.form['cost_unit'] * request.form['quantity']),
            )
            db.add(box)
        except sqlalchemy.exc.IntegrityError as e:
            e = str(e)
            if 'UNIQUE constraint failed: boxes.product_id' in e:
                flash('La Caja ya existe', 'error')
            else:
                flash('Error al agregar Caja', 'error')
        
        return redirect(url_for('products_bp.products'))
    

@products_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = db.get_record(Product, 'product_id', product_id)
    if request.method == 'POST':
        product.product        = request.form['product']
        product.category_id    = request.form['category_id']
        product.cost_unit      = request.form['cost_unit']
        product.inflation_rate = request.form['inflation_rate']
        product.price          = request.form['price']
        db.update(product)
        
        return redirect(url_for('products_bp.products'))
    
@products_bp.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    db.delete_record(Product, 'product_id', product_id)
    return redirect(url_for('products_bp.products'))