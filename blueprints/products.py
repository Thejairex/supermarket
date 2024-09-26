from flask import Blueprint, render_template, request, redirect, url_for, flash

from DB import DB
from DB.models import Product, Category

products_bp = Blueprint('products', __name__)
db = DB()

@products_bp.route('/', methods=['GET', 'POST'])
def products():
    products = db.get_all(Product)
    categories = db.get_all(Category)
    return render_template('products.html', products=products,categories=categories)

@products_bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Product(
            product        = request.form['product'],
            category_id    = request.form['category_id'],
            cost_unit      = request.form['cost_unit'],
            inflation_rate = request.form['inflation_rate'],
            price          = request.form['price']
        )
        db.add(product)
        
        return redirect(url_for('products_bp.products'))
    
    return render_template('add_product.html')

@products_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = db.get_by_column(Product, 'product_id', product_id)
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