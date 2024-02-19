import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Operation:
    date: datetime
    state: str
    card: str
    account: str
    description: str
    operation_amount: dict


    def get_date(self):
        """
        Вывод даты в формате ДД.ММ.ГГГГ
        """
        return self.date.strftime("%d.%m.%Y")
