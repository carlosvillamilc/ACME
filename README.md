# Employee Payment Calculator

### This Python application calculates the amount of money that an employee should be paid based on the hours they worked and the times during which they worked. The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Day of Week | Time | Pay Rate |
| --- | --- | --- |
| Monday - Friday | 00:01 - 09:00 | 25 USD |
| Monday - Friday | 09:01 - 18:00 | 15 USD |
| Monday - Friday | 18:01 - 00:00 | 20 USD |
| Saturday - Sunday | 00:01 - 09:00 | 30 USD |
| Saturday - Sunday | 09:01 - 18:00 | 20 USD |
| Saturday - Sunday | 18:01 - 00:00 | 25 USD |

How to use
To use this application, create a .txt file containing at least five sets of data. Each set of data should include the name of an employee and the schedule they worked, indicating the time and hours. Use the following format:

```
<employee_name>=<day_of_week><start_time>-<end_time>,<day_of_week><start_time>-<end_time>,<day_of_week><start_time>-<end_time>,...
```
Where:

<employee_name> is the name of the employee (string)
<day_of_week> is the day of the week, represented by the following abbreviations:
MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday
<start_time> is the start time in 24-hour format (hh:mm)
<end_time> is the end time in 24-hour format (hh:mm)

For example:

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

Once you have created your input file, run the application with the following command:


python employee_payment_calculator.py <input_file_path>

Where <input_file_path> is the path to your input file.

The application will calculate the amount of money that each employee should be paid and write it into a file in the following format:

<employee_name> is: <amount> USD

Dependencies
This application does not require any external libraries to run. However, you need to create a virtualenvironment for installing pytest and pytest-cov for running the tests. 

Architecture and Approach
