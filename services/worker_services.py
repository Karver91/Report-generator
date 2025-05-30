from core.interfaces.model import ModelInterface
from core.interfaces.service import BaseService
from models.base import Worker
from models.reports import PayoutReport
from repository.base import Repository


class WorkerPayout(BaseService):
    """Отвечает за бизнес-логику для формирования отчета по зарплатам"""
    __report_type = "payout"

    def __init__(
            self,
            repository: Repository,
            model_input=Worker,
            model_output=PayoutReport
    ):
        self.repository = repository
        self.model_input = model_input
        self.model_output = model_output
        super().__init__(repository)

    def process(self):
        data = self.repository.reed_files()
        serialized: list[ModelInterface] = self._serialize_model(data=data, model=self.model_input)
        output = self._get_data_output(data=serialized)
        deserialized: list[dict] = self._deserialize_model(data=output)
        self.repository.write_file(data=deserialized)

    @classmethod
    def get_report_type(cls):
        return cls.__report_type

    def _get_data_output(self, data):
        result = []
        for obj in data:
            payout = self._calculate_salary(rate=obj.rate, hours=obj.hours)
            result.append(
                self.model_output(
                    worker=obj,
                    payout=payout
                )
            )
        return result

    @staticmethod
    def _calculate_salary(rate, hours):
        return rate * hours
