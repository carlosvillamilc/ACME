from src.data.workhours import (weekday_shift_hour_costs,
                                weekend_shift_hour_costs)
from src.domain.worktime import Worktime


class Payment(Worktime):

    def __init__(self, work_day: str, work_schedule: str):

        Worktime.__init__(self, work_day, work_schedule)
        self.payment = 0

    def get_payment(self):

        week_day_type = self.get_day_type()
        shifts = self.get_shift()
        hours = self.get_hours_shift(shifts)

        if week_day_type == 1:
            for index in range(len(hours)):
                cost_per_hour = weekday_shift_hour_costs[shifts[index]]
                self.payment += hours[index] * cost_per_hour
        else:
            for index in range(len(hours)):
                cost_per_hour = weekend_shift_hour_costs[shifts[index]]
                self.payment += hours[index] * cost_per_hour

        return self.payment
