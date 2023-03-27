import os
from src.utils.file_handler import (load_data,
                                    write_data,
                                    input_handler,
                                    output_handler)


class TestFileHandler:

    def teardown_method(self):
        dir_name = os.path.join(os.path.dirname(__file__))
        file_path = os.path.join(dir_name, "employees.txt")

        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist")

    def test_load_data_correct_path(self, file_created, path):
        file_info = load_data(path)
        print(path)
        assert file_info == 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'  # noqa: E501

    def test_load_data_incorrect_path(self):
        file_info = load_data('/employees.txt')
        assert file_info != 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'  # noqa: E501

    def test_write_data_correct_path(self, path):
        output = write_data(path, 'RENE:215')
        with open(path, "r") as f:
            content = f.read()
        assert content == "RENE:215"
        assert output == 8

    def test_input_handler_correct_path(self, file_created):
        dir_name = os.path.dirname(__file__)
        file_info = input_handler(dir_name)
        assert file_info == ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',  # noqa: E501
                             'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']  # noqa: E501

    def test_input_handler_incorrect_path(self, file_created):
        dir_name = os.path.dirname(__file__)
        dir_name = os.path.join(dir_name, "data")
        file_info = input_handler(dir_name)
        assert file_info is None

    def test_output_handler_correct_path(self, file_created):
        dir_name = os.path.dirname(__file__)
        dir_name = os.path.join(dir_name, "data")
        file_info = output_handler('RENE:215', dir_name)
        assert file_info is None
