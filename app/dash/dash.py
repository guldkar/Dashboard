from flask import render_template
from . import db
from datetime import datetime, timedelta
from .models import Customer, Order, Order_item
from itertools import compress


def show_values():
    #dummy data for testing
    #test_data = {'orders':205, 'revenue': 3201, 'customers':140}
    customers = get_data('Customer')
    orders = get_data('Orders')
    order_items = get_data('Order_items')

    revenue = 0
    for o in order_items:
        revenue += o.price

    data = {'orders': len(orders), 'revenue':revenue, 'customers':len(customers)}

    return render_template("dash.html",context=data)



def get_data(table=None):
    query_result = db.query_db('SELECT * FROM {}'.format(table))

    data=[]
    if table == 'Customer':
        for x in query_result:

            data.append( Customer(x[0], x[1], x[2], x[3]) )

    if table == 'Orders':
        for x in query_result:
            data.append( Order(x[0], x[1], x[2], x[3], x[4]) )

    if table == 'Order_items':
        for x in query_result:
            data.append( Order_item(x[0], x[1], x[2], x[3], x[4]) )


    return data

def get_orders(time):
    orders = get_data('Orders')
    today = datetime.today().date()
    if time == 'month':
        timeframe = today - timedelta(days=31)
    if time == 'week':
        timeframe = today - timedelta(days=7)

    filter = []
    for x in orders:
        filter.append(x.purchase_date > timeframe)
    orders = list(compress(orders, filter))
    return orders

def get_customers(orders):
    customer_ids = []
    for x in orders:
        customer_ids.append(x.customer_id)
    print("amount of customers: ",len(set(customer_ids)))
    return len(set(customer_ids))

def get_revenue(orders):
    order_ids = []
    for x in orders:
        order_ids.append(x.id)
    order_items = get_data('Order_items')
    order_items = [o for o in order_items if o.order_id in order_ids]
    revenue =0
    for o in order_items:
        revenue += o.price
    print(order_items)
    return revenue

def get_field_data(field, time):
    orders=get_orders(time)
    if field == 'Orders':
        return len(orders)

    if field == 'Customers':
        customers = get_customers(orders)
        return customers

    if field == 'Revenue':
        revenue = get_revenue(orders)
        return revenue