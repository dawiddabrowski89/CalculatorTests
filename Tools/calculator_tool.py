import re
import random

buttons_id = {
    '0': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_00',
    '1': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_01',
    '2': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_02',
    '3': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_03',
    '4': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_04',
    '5': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_05',
    '6': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_06',
    '7': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_07',
    '8': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_08',
    '9': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_09'
}

operations_id = {
    '+': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_add',
    '-': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub',
    '*': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_mul',
    '/': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_div'
}


def click_digits(driver: 'webdriver', digit: 'str') -> None:
    for i in digit:
        chosen_digit = driver.find_element_by_id(buttons_id[i])
        chosen_digit.click()
        result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
        assert re.match(".*" + i + ".*", result), "Wrong value for first digit"


def click_operator(driver: 'webdriver', operator: 'str') -> None:
    op_add = driver.find_element_by_id(operations_id[operator])
    op_add.click()
    result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
    if operator == '+':
        assert re.match(".*\\+.*", result), "Wrong value for operator"


def click_equal(driver: 'webdriver', correct_result: 'str') -> None:
    equal = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal")
    equal.click()
    result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
    print("Result:" + result)
    print("Correct result:" + correct_result)
    assert re.match(".*" + correct_result + ".*", result), "Wrong value for sum"


def generate_data(digit_range: int = 10, number_of_tests: int = 3) -> 'List':
    """
        Return the list of test variants
        Operations:
            1 - addition
            2 - subtraction
            3 - multiplication
            4 - division
    """
    list_of_tests = []
    for i in range(number_of_tests):
        # operator = random.randint(1, 4)
        operator = 1
        operator_char = None
        first_digit = random.randint(0, digit_range)
        second_digit = random.randint(0, digit_range)
        if operator == 1:
            result = first_digit + second_digit
            operator_char = '+'
        elif operator == 2:
            result = first_digit - second_digit
            operator_char = '-'
        elif operator == 3:
            result = first_digit * second_digit
            operator_char = '*'
        elif operator == 4:
            result = first_digit / second_digit
            result = round(result)
            operator_char = '/'

        test = (str(first_digit), str(second_digit), str(result), operator_char)
        list_of_tests.append(test)
    return list_of_tests
