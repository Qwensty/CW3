import pytest
from utils import get_data, get_sorted_data, get_last_values, get_formatted_data


def test_get_data(test_link):
    assert len(get_data(test_link)[0]) > 0
    assert get_data("https://strq.url.com/")[0] is None
    assert get_data("https://github.com/Qwensty/python_project")[0] is None
    assert get_data("https://github.com/Qwensty/python_project")[0] is None


def test_get_sorted_data(test_data):
    assert len(get_sorted_data(test_data)) == 4
    assert len(get_sorted_data(test_data, missing_sander=True)) == 2


def test_get_limit_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]["date"] == '2020-09-03T18:35:29.512364'
    assert len(data) == 4



def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['    26.08.2019 Перевод организации\n    Maestro 1596 83** **** 5199 -> Счет **9589\n    31957.58 руб.', '    03.09.2020 Перевод организации\n      -> Счет **5560\n    8221.37 USD', '    30.06.2018 Перевод организации\n    Счет 7510 68** **** 6952 -> Счет **6702\n    9824.07 USD', '    23.03.2018 Открытие вклада\n      -> Счет **2431\n    48223.05 руб.', '    04.04.2019 Перевод со счета на счет\n    Счет 1970 86** **** 8542 -> Счет **4188\n    79114.93 USD']


