import pytest
import os

from src.domain.worktime import Worktime

@pytest.fixture
def path():
      dir_name = os.path.join( os.path.dirname( __file__ ))
      file_path = os.path.join(dir_name, "employees.txt")
      return file_path


@pytest.fixture
def file_created(path):
    
      file_data = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
      with open(path, "a+") as file:
            file.write(file_data)


@pytest.fixture
def correct_employee_input():      
      return 'RENE=MO10:00-12:00,TU10:00-12:00'

@pytest.fixture
def worktime_weekday_ten_twelve():
      return Worktime('MO','10:00-12:00')

@pytest.fixture
def worktime_weekend_ten_twelve():
      return Worktime('SU','10:00-12:00')

@pytest.fixture
def worktime_weekend_seven_twelve():
      return Worktime('SU','07:00-12:00')