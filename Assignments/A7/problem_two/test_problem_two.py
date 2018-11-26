# unit test for month_length function written in problem_two.py

import problem_two

def test_problem_two():
    assert problem_two.month_length("January") == 31, "failed for 31 days month, January"
    assert problem_two.month_length("September") == 30, "failed for 30 days month, September"
    assert problem_two.month_length("February", leap_year = True) == 29, "failed for February month in leap year"
    assert problem_two.month_length("February", leap_year = False) == 28, "failed for February month without leap year"
