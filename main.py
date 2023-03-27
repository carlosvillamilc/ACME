import sys

from src.domain.payment import Payment
from src.utils.file_handler import input_handler, output_handler
from src.utils.data_handler import get_schedule_data
from src.domain.payment import Payment


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            print('Incomplete Arguments')            
            raise SystemExit

        file_path = str(sys.argv[1])
        
        employees_rows = input_handler(file_path)
        for employee_schedule in employees_rows:
            data_list = get_schedule_data(employee_schedule)
            name = data_list[0]
            payment = 0
            for data in data_list[1:]:                
                payment += Payment(data[0:2],data[2:]).get_payment()
            print(f'{name}:{payment}\n')
            output_handler(f'{name}:{payment}\n',file_path)
        
    except Exception as error:
        print('Error:', error)