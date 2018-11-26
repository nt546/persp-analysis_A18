# unit test for operate function written in problem_three.py

import pytest
import problem_three

def test_operator_rep():
    with pytest.raises(TypeError) as excinfo:
        problem_three.operate(4, 2, 1)
    assert excinfo.value.args[0] == "oper must be a string"

def test_add():
    assert problem_three.operate(1, 3, "+") == 4, "failed on positive integers"
    assert problem_three.operate(-5, -7, "+") == -12, "failed on negative integers"
    assert problem_three.operate(-6, 14, "+") == 8, "failed on positive and negative integer combination"

def test_subtract():
    assert problem_three.operate(1, 3, "-") == -2, "failed on positive integers"
    assert problem_three.operate(-5, -7, "-") == 2, "failed on negative integers"
    assert problem_three.operate(-6, 14, "-") == -20, "failed on positive and negative integer combination"

def test_multiply():
    assert problem_three.operate(1, 0, "*") == 0, "failed on multiplication with 0"
    assert problem_three.operate(1, 3, "*") == 3, "failed on positive integers"
    assert problem_three.operate(-5, -7, "*") == 35, "failed on negative integers"
    assert problem_three.operate(-6, 14, "*") == -84, "failed on positive and negative integer combination"

def test_divide():
    assert problem_three.operate(4, 2, "/") == 2, "integer division"
    assert problem_three.operate(5, 4, "/") == 1.25, "float division"
    with pytest.raises(ZeroDivisionError) as excinfo:
        problem_three.operate(4, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"

def test_operator_types():
    with pytest.raises(ValueError) as excinfo:
        problem_three.operate(4, 2, "%")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
