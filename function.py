import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def json_to_list(jsonfile):
    """
    ф-я конвертирует json в list
    :param jsonfile:
    :return:
    """
    with open(jsonfile, "r") as file:
        conv_dict = json.load(file)  # конвертируем json в словарь
    return conv_dict

