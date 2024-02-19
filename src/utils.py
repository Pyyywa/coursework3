import json
from src.operation import Operation
from datetime import datetime

def load_data():

    with open("../data/operations.json", encoding='utf-8') as file:
        all_operations = json.load(file)

    operations = []
    for operation in all_operations:
        if not operation:
            continue

        operation = Operation(
            date = datetime.fromisoformat(operation['date']),
            state=operation['state'],
            description = operation['description'],
            card = operation.get('from', 'Unknown'),
            account = operation['to'],
            operation_amount = operation['operationAmount']
            )
        operations.append(operation)

    return operations

def masks(card_number):
    """
    Возвращает замаскированные номера счетов
    и карт отправителя/получателя (если они существуют).
    """

    if 'Счет' in card_number:
        masked_number = card_number[:5] + '**' + card_number[-4:]
        return masked_number
    elif 'Unknown' in card_number:
        return 'Unknown'
    else:
        masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + \
                        card_number[-12:-10] + '** **** ' + card_number[-4:]
        return masked_number


def filter_and_sorting(*operations: Operation) -> list:
    """
    Сортирует выполненные операции по дате
    """
    items = [item for item in operations if item.state == 'EXECUTED']
    items.sort(key = lambda x: x.date, reverse = True)
    return items


def msg_output(*operations) -> str:
    """
    Выводит информацию в необходимом формате
    """
    sorted_op = filter_and_sorting(*operations)

    for operation in sorted_op[:5]:

        from_op = masks(operation.card)
        to_op = masks(operation.account)
        amount = operation.operation_amount['amount']
        currency = operation.operation_amount['currency']['name']

        output = f"{operation.get_date()} {operation.description}\n"\
                 f"{from_op} -> {to_op}\n"
        f"{amount} {currency}\n"
        print(output)