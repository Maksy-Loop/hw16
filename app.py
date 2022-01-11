from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from funforflask import get_all_users, get_user, get_all_orders, get_order, get_all_offers, get_offer
import sql
import json
from function import json_to_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

@app.route("/users", methods=["GET", "POST"])
def page_users():
    if request.method == "GET":
        return jsonify(get_all_users())
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")
        email = request.form.get("email")
        role = request.form.get("role")
        phone = request.form.get("phone")

        if first_name and last_name and age and email and role and phone:
            user = sql.Users(first_name=first_name, last_name=last_name, age=age,
                                 email=email, role=role, phone=phone)
            db.session.add(user)
            db.session.commit()

            return "Пользователь добален"
        else:
            return "Отправка не корректная"


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_users_id(id):
    if request.method == "GET":
        return jsonify(get_user(id))

    if request.method == "PUT":

        dict_json = request.json

        user = db.session.query(sql.Users).get(id)

        user.first_name = dict_json.get("first_name")
        user.last_name = dict_json.get("last_name")
        user.age = dict_json.get("age")
        user.email = dict_json.get("email")
        user.role = dict_json.get("role")
        user.phone = dict_json.get("phone")

        db.session.add(user)
        db.session.commit()
        return f'Данные перезаписаны'

    if request.method == "DELETE":
        user = db.session.query(sql.Users).get(id)
        db.session.delete(user)
        db.session.commit()

        return f'Пользователь удален'


@app.route("/orders", methods=["GET", "POST"])
def page_orders():
    if request.method == "GET":
        return jsonify(get_all_orders())

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        address = request.form.get("address")
        price = request.form.get("price")
        customer_id = request.form.get("customer_id")
        executor_id = request.form.get("executor_id")

        if name and description and start_date and end_date and address and price and customer_id and executor_id:
            order = sql.Users(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                address=address,
                price=price,
                customer_id=customer_id,
                executor_id=executor_id
            )
            db.session.add(order)
            db.session.commit()

            return "Заказ добален"
        else:
            return "Отправка не корректная"


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_order_id(id):

    if request.method == "GET":
        return jsonify(get_order(id))

    if request.method == "PUT":

        dict_json = request.json

        order = db.session.query(sql.Orders).get(id)

        order.name = dict_json.get("name")
        order.description = dict_json.get("description")
        order.start_date = dict_json.get("start_date")
        order.end_date = dict_json.get("end_date")
        order.address = dict_json.get("address")
        order.price = dict_json.get("price")
        order.customer_id = dict_json.get("customer_id")
        order.executor_id = dict_json.get("executor_id")

        db.session.add(order)
        db.session.commit()
        return f'Данные перезаписаны'

    if request.method == "DELETE":
        user = db.session.query(sql.Orders).get(id)
        db.session.delete(user)
        db.session.commit()

        return f'Заказ удален'


@app.route("/offers", methods=["GET", "POST"])
def page_offers():

    if request.method == "GET":
        return jsonify(get_all_offers())

    if request.method == "POST":
        order_id = request.form.get("order_id")
        executor_id = request.form.get("executor_id")

        if order_id and executor_id:
            offer = sql.Offers(order_id=order_id, executor_id=executor_id)
            db.session.add(offer)
            db.session.commit()

            return "Оффер добален"
        else:
            return "Отправка не корректная"


@app.route("/offers/<int:id>", methods=["GET", "PUT", "DELETE"])
def page_offer_id(id):

    if request.method == "GET":
        return jsonify(get_offer(id))

    if request.method == "PUT":

        dict_json = request.json

        offer = db.session.query(sql.Offers).get(id)

        offer.order_id = dict_json.get("order_id")
        offer.executor_id = dict_json.get("executor_id")

        db.session.add(offer)
        db.session.commit()
        return f'Данные перезаписаны'

    if request.method == "DELETE":
        offer = db.session.query(sql.Offers).get(id)
        db.session.delete(offer)
        db.session.commit()

        return f'Оффер удален'


if __name__ == "__main__":
    app.run(debug=True)