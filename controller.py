from core.interfaces.service import ServiceInterface


class ExecutionController:
    def __init__(self, service):
        self.service: ServiceInterface = service

    def run(self):
        self.service.process()
