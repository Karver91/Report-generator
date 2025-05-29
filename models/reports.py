from core.interfaces.model import ModelInterface
from enums import CurrencySymbol
from models.base import Worker


class PayoutReport(ModelInterface):
    """Модель отчета по заработной плате"""

    def __init__(
            self,
            worker: Worker,
            payout: int
    ):
        self.worker = worker
        self.payout = f"{CurrencySymbol.USD}{payout}"

    def to_dict(self) -> dict:
        d = self.worker.to_dict()
        d["payout"] = self.payout
        return d

    def validate(self, name, value):
        ...


class DepartmentHourlyRateReport(ModelInterface):
    """Модель отчета со средней ставкой в час по отделам"""

    def to_dict(self) -> dict:
        ...

    def validate(self, name, value):
        ...
