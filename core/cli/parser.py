import argparse

from core.interfaces.service import BaseService


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--report",
                        help=f"Тип отчёта для генерации. "
                             f"Варианты: {[service.get_report_type() for service in BaseService.__subclasses__()]}",
                        default="payout")
    parser.add_argument("files", nargs="+", help="Пути к файлам с данными")
    parser.add_argument("-o", "--output", type=str, help="Путь к файлу отчета", default="report")
    return parser
