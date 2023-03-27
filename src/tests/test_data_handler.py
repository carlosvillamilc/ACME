from src.utils.data_handler import get_schedule_data


class TestDataHandler:

    def teardown_method(self):
        pass

    def test_get_schedule_data_correct_format_input(self,
                                                    correct_employee_input):
        result = get_schedule_data(correct_employee_input)
        assert result == ['RENE', 'MO10:00-12:00', 'TU10:00-12:00']
