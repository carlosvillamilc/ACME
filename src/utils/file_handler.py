import os


def load_data(path: str) -> str:
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('File not Found')


def write_data(path: str, payment_info: str) -> int:
    try:
        with open(path, "a+") as file:
            return file.write(payment_info)
    except FileNotFoundError:
        print('File not Found')


def input_handler(dir_name: str) -> list:
    file_path = os.path.join(dir_name, "employees.txt")
    data = load_data(file_path)
    if data is not None:
        return data.split('\n')


def output_handler(payment_info: str, dir_name: str) -> int:
    file_path = os.path.join(dir_name, "payment.txt")
    return write_data(file_path, payment_info)
