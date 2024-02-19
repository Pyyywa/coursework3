import pytest
from datetime import datetime
from src.operation import Operation

def test_get_date():
    operation = Operation(datetime(2019, 8, 26, 10, 50, 58, 294041),
                          card='Maestro 1596837868705199', account='Счет 35383033474447895560',
                          state='EXECUTED', description='Перевод организации',
                          operation_amount={'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}})
    assert Operation.get_date(operation) == "26.08.2019"

