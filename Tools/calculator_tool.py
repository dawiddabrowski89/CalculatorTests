import math
import random
from os import truncate

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
    '−': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub',
    '×': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_mul',
    '÷': 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_div'
}


def click_digits(driver: 'webdriver', digit: 'str') -> None:
    for i in digit:
        chosen_digit = driver.find_element_by_id(buttons_id[i])
        chosen_digit.click()
        result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
        assert i in result, "Wrong value for digit"


def click_operator(driver: 'webdriver', operator: 'str') -> None:
    op_add = driver.find_element_by_id(operations_id[operator])
    op_add.click()
    result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
    assert operator in result, "Wrong value for operator"


def click_equal(driver: 'webdriver', correct_result: 'str') -> None:
    equal = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal")
    equal.click()
    result = driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_edt_formula").text
    print("Correct result: " + correct_result)
    print("Real result: " + result)
    assert correct_result in result, "Wrong value for operation"


def round_down(n: int, decimals: int = 0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def result_parser(result):
    if len(result) > 3:
        list_temp = list(reversed(result))
        k = 0
        space = 0
        for i in list_temp:
            k += 1
            space += 1
            if i == ",":
                space = 0
            if space == 4:
                list_temp.insert(k-1, " ")
                space = 0
        list_temp.reverse()
        result = ""
        for i in list_temp:
            result += i
    return result


def generate_data(digit_range: int = 100, number_of_tests: int = 100) -> 'List':
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
        operator = random.randint(1, 4)
        operator_char = None
        first_digit = random.randint(0, digit_range)
        second_digit = random.randint(0, digit_range)
        while operator == 4 and second_digit == 0:
            second_digit = random.randint(0, digit_range)
        if operator == 1:
            result = first_digit + second_digit
            operator_char = '+'
        elif operator == 2:
            result = first_digit - second_digit
            if result < 0:
                result = '−' + str(abs(result))
            operator_char = '−'
        elif operator == 3:
            result = first_digit * second_digit
            operator_char = '×'
        elif operator == 4:
            result = first_digit / second_digit
            if result.is_integer():
                result = str(int(result))
            else:
                result = str(round_down(result, 2))
            if '.' in result:
                result = result.replace('.', ',')
            operator_char = '÷'
        test = (str(first_digit), str(second_digit), result_parser(str(result)), operator_char)
        list_of_tests.append(test)
    return list_of_tests
