import calculator_tool
import pytest


class TestCalculator:
    @pytest.mark.parametrize("digit_1, digit_2, correct_result, operator",
                             calculator_tool.generate_data())
    def test_calculator(self, connect_to_device, digit_1, digit_2, correct_result, operator):
        driver = connect_to_device
        calculator_tool.click_digits(driver, digit_1)
        calculator_tool.click_operator(driver, operator)
        calculator_tool.click_digits(driver, digit_2)
        calculator_tool.click_equal(driver, correct_result)
