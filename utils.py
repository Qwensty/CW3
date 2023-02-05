import requests
from datetime import datetime


def get_data(url):
    """
    Функция для получения данных (с учетом возможных ошибок)
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно\n"
        return None, f"ERROR: status_code:{response.status_code}"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError\n"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError\n"



def get_sorted_data(data, missing_sander=False):
    """
    Функция для обработки данных

    :return: Обработанные данные по параметрам state и from
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if missing_sander:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    """
    Функция для получения данных и с лимитом в 5 значений
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    """
    Функция для форматирования данных в определенный формат

    :return:Данные в формате
             <дата перевода> <описание перевода>
             <откуда> -> <куда>
             <сумма перевода> <валюта>
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        from_info, from_account = "", ""
        if "from" in row:
            sender = row["from"].split()
            from_account = sender.pop(-1)
            from_account = f"{from_account[:4]} {from_account[4:6]}** **** {from_account[-4:]}"
            from_info = " ".join(sender)
        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
    {date} {description}
    {from_info} {from_account} -> {to}
    {operation_amount}""")

    return formatted_data
