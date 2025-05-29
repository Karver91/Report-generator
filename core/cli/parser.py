import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--report", help="Тип отчёта для генерации", default="report")
    parser.add_argument("files", nargs="+", help="Пути к CSV-файлам с данными")
    return parser
