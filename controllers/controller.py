from app import banana
from flask import render_template
from modules.order_list import orders as all_orders

@banana.route('/orders')
def orders():
    return render_template('index.html', title='My list of orders', all_orders=all_orders)