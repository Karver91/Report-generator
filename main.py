from argparse import ArgumentParser, Namespace

from controller import ExecutionController
from core.cli.parser import get_parser
from core.interfaces.service import ServiceInterface
from repository.base import Repository
from services.worker_services import WorkerPayout


def main():
    cli_parser: ArgumentParser = get_parser()
    args: Namespace = cli_parser.parse_args()

    repository: Repository = Repository(files=args.files, report=args.report)
    service: ServiceInterface = WorkerPayout(repository=repository)
    controller = ExecutionController(service=service)
    controller.run()


if __name__ == '__main__':
    main()
