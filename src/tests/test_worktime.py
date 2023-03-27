

class TestWorktime:

    def teardown_method(self):
        pass

    def test_get_day_type_weekday(self, worktime_weekday_ten_twelve):
        assert worktime_weekday_ten_twelve.get_day_type() == 1

    def test_get_day_type_weekend(self, worktime_weekend_ten_twelve):
        assert worktime_weekend_ten_twelve.get_day_type() == 0

    def test_get_shift_one_shift_work(self, worktime_weekday_ten_twelve):
        assert (worktime_weekday_ten_twelve.get_shift() ==
               ['second_shift', 'second_shift'])

    def test_get_shift_two_shift_work(self, worktime_weekend_seven_twelve):
        assert (worktime_weekend_seven_twelve.get_shift() ==
                ['first_shift', 'second_shift'])

    def test_get_hours_shift_one_shift_work(self, worktime_weekday_ten_twelve):
        assert (worktime_weekday_ten_twelve.get_hours_shift(
               worktime_weekday_ten_twelve.get_shift()) == [2])

    def test_get_hours_shift_two_shift_work(self, worktime_weekend_seven_twelve):  # noqa: E501
        assert (worktime_weekend_seven_twelve.get_hours_shift(
          worktime_weekend_seven_twelve.get_shift()) == [2, 3])
