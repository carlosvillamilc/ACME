from src.data.workhours import shift_hours, weekday
from datetime import datetime


class Worktime:
    def __init__(self, work_day: str, work_schedule: str):
        self.work_day = work_day
        self.work_schedule = work_schedule

    def get_day_type(self) -> int:
        if self.work_day in weekday:
            return 1
        else:
            return 0

    def get_shift(self) -> list:
        hours = self.work_schedule.split('-')

        for shift_hour in shift_hours:
            if (shift_hours[shift_hour][1] >
                    hours[0] >=
                    shift_hours[shift_hour][0]):

                starting_shift = shift_hour
            if (shift_hours[shift_hour][1] >=
                    hours[1] >
                    shift_hours[shift_hour][0]):

                ending_shift = shift_hour

        return [starting_shift, ending_shift]

    def get_hours_shift(self, shift: list) -> list:

        hours = self.work_schedule.split('-')

        start_hour = datetime.strptime(hours[0], '%H:%M')
        finish_hour = datetime.strptime(hours[1], '%H:%M')

        if shift[0] != shift[1]:
            # finish time
            finish_time_starting_shift = shift_hours[shift[0]][1]

            finish_hour_starting_shift = datetime.strptime(
                                        finish_time_starting_shift,
                                        '%H:%M')

            starting_shift_time = (finish_hour_starting_shift.hour -
                                   start_hour.hour)
            finish_shift_time = (finish_hour.hour -
                                 finish_hour_starting_shift.hour)
            return [starting_shift_time, finish_shift_time]

        return [finish_hour.hour-start_hour.hour]
