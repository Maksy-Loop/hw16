from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime as DT
from function import json_to_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


class Offers(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))



db.create_all()
#db.drop_all()

# реазизовали функции чтобы положить данные json в базу
def add_data_to_users(list):
    db_row = []
    for row in list:
        element = Users(id=row["id"], first_name=row["first_name"], last_name=row["last_name"],
                     age=row["age"], email=row["email"], role=row["role"], phone=row["phone"])
        db_row.append(element)

    db.session.add_all(db_row)
    db.session.commit()

    return print("done")

def add_data_to_offers(list):
    db_row = []
    for row in list:
        element = Offers(id=row["id"], order_id=row["order_id"], executor_id=row["executor_id"])
        db_row.append(element)

    db.session.add_all(db_row)
    db.session.commit()

    return print("done")

def add_data_to_orders(list):
    db_row = []
    for row in list:
        new_start_date = DT.datetime.strptime(row["start_date"], '%m/%d/%Y').date()
        new_finish_date = DT.datetime.strptime(row["end_date"], '%m/%d/%Y').date()
        element = Orders(id=row["id"], name=row["name"], description=row["description"],
                         start_date=new_start_date, end_date=new_finish_date,
                         address=row["address"], price=row["price"], customer_id=row["customer_id"],
                         executor_id=row["executor_id"])
        db_row.append(element)

    db.session.add_all(db_row)
    db.session.commit()

    return print("done")

#c помощью вызовов функций ниже мы положили данные в базы

#add_data_to_users(json_to_list("users.json"))
#add_data_to_offers(json_to_list("offers.json"))
#add_data_to_orders(json_to_list("orders.json"))















#if __name__ == "__main__":
  #  app.run(debug=True)