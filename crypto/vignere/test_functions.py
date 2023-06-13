""" Helper functions for tests
"""


def test_result(test_condition_pass: bool):
    """ Helper function for printing pass/fail results
    """
    return "pass" if test_condition_pass else "fail"
