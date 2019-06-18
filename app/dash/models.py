from . import db
from datetime import datetime



class Customer:
    def __init__(self, id, first_name, last_name, email):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email


class Order:
    def __init__(self,id, customer_id, purchase_date, country, device):
        self.id=id
        self. customer_id=customer_id
        self.purchase_date= datetime.strptime(purchase_date, '%d-%m-%y').date()
        self.country=country
        self.device=device


class Order_item:
    def __init__(self, id, order_id, EAN, quantity, price):
        self.id=id
        self.order_id=order_id
        self.EAN=EAN
        self.quantity=quantity
        self.price=price




