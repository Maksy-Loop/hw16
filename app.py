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


@app.route("/orders")
def page_orders():
    return jsonify(get_all_orders())

@app.route("/orders/<int:id>")
def page_order_id(id):
    return jsonify(get_order(id))


@app.route("/offers")
def page_offers():
    return jsonify(get_all_offers())

@app.route("/offers/<int:id>")
def page_offer_id(id):
    return jsonify(get_offer(id))







if __name__ == "__main__":
    app.run(debug=True)