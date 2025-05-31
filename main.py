import sys
from argparse import ArgumentParser, Namespace

from controller import ExecutionController
from core.cli.parser import get_parser
from repository.base import Repository
from views.cli import CLIView


def main():
    sys.argv = ['main.py', '/home/oleg/PythonProject/test_tasks/Workmate/tests/testing_data/data1.csv']

    cli_parser: ArgumentParser = get_parser()
    args: Namespace = cli_parser.parse_args()
    view = CLIView()
    repository: Repository = Repository(files=args.files, output=args.output)
    controller = ExecutionController(report=args.report, repository=repository, view=view)
    controller.run()


if __name__ == '__main__':
    main()
