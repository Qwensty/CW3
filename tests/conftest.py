import pytest


@pytest.fixture
def test_link():
    return "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230205T093436Z&X-Amz-Expires=86400&X-Amz-Signature=71e20bf8c6eb51ec9f912a5e2b44f4492328502f724244e4c0b6744722adc06c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"


@pytest.fixture
def test_data():
    return [{'date': '2019-08-26T10:50:58.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596837868705199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'to': 'Счет 64686473678894779589'},
 {'date': '2020-09-03T18:35:29.512364',
  'description': 'Перевод организации',
  'id': 41428829,
  'operationAmount': {'amount': '8221.37',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35383033474447895560'},
 {'date': '2018-06-30T02:08:58.425572',
  'description': 'Перевод организации',
  'from': 'Счет 75106830613657916952',
  'id': 939719570,
  'operationAmount': {'amount': '9824.07',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 11776614605963066702'},
 {'date': '2018-03-23T10:45:06.972075',
  'description': 'Открытие вклада',
  'id': 587085106,
  'operationAmount': {'amount': '48223.05',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 41421565395219882431'},
 {'date': '2019-04-04T23:20:05.206878',
  'description': 'Перевод со счета на счет',
  'from': 'Счет 19708645243227258542',
  'id': 142264268,
  'operationAmount': {'amount': '79114.93',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 75651667383060284188'}]


