from flask import Blueprint, render_template, request, redirect, url_for, flash

from DB import DB
from DB.models import Product

products_bp = Blueprint('products', __name__)
db = DB()

@products_bp.route('/')
def products():
    products = db.get_all(Product)
    return render_template('products.html', products=products)

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
        
        return redirect(url_for('products'))
    
    return render_template('add_product.html')