import os


def get_schedule_data(schedule:str) -> list:
    employee_data = schedule.split('=')
    name = employee_data[0]    
    employee_schedule = employee_data[1].split(',')
    result = [name]
    result.extend(employee_schedule)
    return result