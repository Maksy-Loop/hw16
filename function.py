import json

def json_to_list(jsonfile):
    """
    ф-я конвертирует json в list
    :param jsonfile:
    :return:
    """
    with open(jsonfile, "r") as file:
        conv_dict = json.load(file)  # конвертируем json в словарь
    return conv_dict



