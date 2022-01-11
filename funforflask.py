from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#функции для пост запроса к роутам, вытягивают всех пользователей или по айди
def get_all_users():
    user = db.session.query(sql.Users).all()
    list_users = []
    for row in user:
        dict_row = {
            "id":row.id,
            "first_name":row.first_name,
            "last_name":row.last_name,
            "age":row.age,
            "email":row.email,
            "role":row.role,
            "phone":row.phone
        }
        list_users.append(dict_row)

    return list_users

def get_user(id):
    user = db.session.query(sql.Users).get(id)

    if user is None:
        return "Такого пользователя нет"


    user_dict = {
            "id":user.id,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "age":user.age,
            "email":user.email,
            "role":user.role,
            "phone":user.phone
        }

    return user_dict

def get_all_orders():
    order = db.session.query(sql.Orders).all()
    list_orders = []
    for row in order:
        dict_row = {
            "id":row.id,
            "name":row.name,
            "description":row.description,
            "start_date":row.start_date,
            "end_date":row.end_date,
            "address":row.address,
            "price":row.price,
            "customer_id": row.customer_id,
            "executor_id": row.executor_id
        }
        list_orders.append(dict_row)

    return list_orders

def get_order(id):
    order = db.session.query(sql.Orders).get(id)

    if order is None:
        return "Такого заказа нет"

    user_dict = {
            "id":order.id,
            "name":order.name,
            "description":order.description,
            "start_date":order.start_date,
            "end_date":order.end_date,
            "address":order.address,
            "price":order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }

    return user_dict

def get_all_offers():
    offer = db.session.query(sql.Offers).all()
    list_offers = []
    for row in offer:
        dict_row = {
            "id":row.id,
            "order_id":row.order_id,
            "executor_id":row.executor_id
        }
        list_offers.append(dict_row)

    return list_offers

def get_offer(id):
    offer = db.session.query(sql.Offers).get(id)

    if offer is None:
        return "Такого оффера нет"

    offer_dict = {
            "id":offer.id,
            "order_id":offer.order_id,
            "executor_id":offer.executor_id
        }

    return offer_dict
