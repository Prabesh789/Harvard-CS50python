import pytest

from calculate import square
'''
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
'''
'''
This whole test is automate by pytest library

install the pytest: pip install pytest
and follow as above.

run cmd pytest test_calculator.py

# def main():

#     def test_square():
#         try:
#             assert square(2) == 4
#         except AssertionError:
#             print("2 squared was not 4")
#         try:
#             assert square(3) == 9
#         except AssertionError:
#             print("2 squared was not 4")

# if __name__ == "__main__":
#     main()
'''


# spearating big test to multiple test
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# test for string input, here square function is not wrong but there is type error
def test_str():
    with pytest.raises(TypeError):
        square("cat")
