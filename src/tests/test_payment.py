import os
import pytest
from src.utils.file_handler import (load_data, 
                                    write_data,
                                    input_handler,
                                    output_handler)

class TestPayment:

    def teardown_method(self):
        pass


    def test_get_payment_type_weekday(self,payment_weekday_ten_twelve):
         assert payment_weekday_ten_twelve.get_payment() == 30

    def test_get_payment_type_weekend(self,payment_weekend_ten_twelve):
         assert payment_weekend_ten_twelve.get_payment() == 40
         