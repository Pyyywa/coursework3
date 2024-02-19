import pytest
from datetime import datetime
from src.utils import load_data, msg_output, masks, filter_and_sorting
from src.operation import Operation

def test_load_data():
    assert isinstance(load_data(), list)

def test_masks(bank_fixture_1, bank_fixture_2, bank_fixture_3):
    assert masks(bank_fixture_1) == "Maestro 1596 83** **** 5199"
    assert masks(bank_fixture_2) == "Счет **3493"
    assert masks(bank_fixture_3) == "Unknown"

def test_filter_and_sorting(op_1):
    operations = []

    for operation in op_1:
        operation = Operation(
            date=datetime.fromisoformat(operation['date']),
            state=operation['state'],
            description=operation['description'],
            card=operation.get('from', 'Unknown'),
            account=operation['to'],
            operation_amount=operation['operationAmount']
        )
        operations.append(operation)
        return operations

    assert filter_and_sorting(operations) == ("[Operation(date=datetime.datetime(2019, 8, 26, 10, 50, 58, 294041), "
                                              "state='EXECUTED', card='Maestro 1596837868705199', "
                                              "account='Счет 64686473678894779589', "
                                              "description='Перевод организации', "
                                              "operation_amount={'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}), "
                                              "Operation(date=datetime.datetime(2019, 7, 3, 18, 35, 29, 512364), "
                                              "state='EXECUTED', card='MasterCard 7158300734726758', "
                                              "account='Счет 35383033474447895560', "
                                              "description='Перевод организации', "
                                              "operation_amount={'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}), "
                                              "Operation(date=datetime.datetime(2018, 6, 30, 2, 8, 58, 425572), "
                                              "state='EXECUTED', card='Счет 75106830613657916952', "
                                              "account='Счет 11776614605963066702', "
                                              "description='Перевод организации', "
                                              "operation_amount={'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}), "
                                              "Operation(date=datetime.datetime(2018, 3, 23, 10, 45, 6, 972075), "
                                              "state='EXECUTED', card='Unknown', account='Счет 41421565395219882431', "
                                              "description='Открытие вклада', "
                                              "operation_amount={'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}})]")