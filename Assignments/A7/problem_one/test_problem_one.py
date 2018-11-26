# unit test for smallest_factor function written in problem_one.py

import problem_one

def test_problem_one():
    assert problem_one.smallest_factor(1) == 1, "failed for integer 1"
    assert problem_one.smallest_factor(3) == 3, "failed for prime numbers"
    assert problem_one.smallest_factor(6) == 2, "failed for even composite numbers"
    assert problem_one.smallest_factor(15) == 3, "failed for odd composite numbers"
