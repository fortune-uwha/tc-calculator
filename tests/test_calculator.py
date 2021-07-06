from calculator.calculator import Calculator
import pytest

# Fixtures


@pytest.fixture
def calculator():
    return Calculator()


# Helpers


def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer

# Test Cases


def test_last_answer_init(calculator):
    assert calculator.last_answer == 0


def test_verify_input(calculator):
    with pytest.raises(ValueError) as error:
        calculator.verify_input('ab')
    assert "This is not a number" in str(error)


def test_add(calculator):
    answer = calculator.add(9)
    verify_answer(9, answer, calculator.last_answer)


def test_subtract(calculator):
    answer = calculator.subtract(9)
    verify_answer(-9, answer, calculator.last_answer)


def test_subtract_negative(calculator):
    answer = calculator.subtract(-9)
    verify_answer(9, answer, calculator.last_answer)


def test_multiply(calculator):
    answer = calculator.multiply(9)
    verify_answer(0, answer, calculator.last_answer)


def test_divide(calculator):
    calculator = Calculator(last_answer=9)
    answer = calculator.divide(3)
    verify_answer(3, answer, calculator.last_answer)


def test_divide_by_zero(calculator):
    calculator = Calculator(last_answer=9)
    with pytest.raises(ZeroDivisionError) as error:
        calculator.divide(0)
    assert "You cannot divide by zero" in str(error)


def test_nroot(calculator):
    calculator = Calculator(last_answer=4)
    answer = calculator.nroot(2)
    verify_answer(2, answer, calculator.last_answer)


def test_nroot_negative_root(calculator):
    calculator = Calculator(last_answer=4)
    answer = calculator.nroot(-2)
    verify_answer(0.5, answer, calculator.last_answer)


def test_nroot_zero(calculator):
    with pytest.raises(ZeroDivisionError) as error:
        calculator.nroot(0)
    assert "Please provide a non-zero number" in str(error)


def test_nroot_negative_last_answer(calculator):
    calculator = Calculator(last_answer=-4)
    with pytest.raises(ValueError) as error:
        calculator.nroot(2)
    assert "Calculator cannot take nth root of a negative number" in str(error)


def test_last_answer(calculator):
    calculator.add(9)
    answer = calculator.last_answer
    verify_answer(9.0, answer, calculator.last_answer)


def test_reset_memory(calculator):
    answer = calculator.reset_memory()
    verify_answer(0.0, answer, calculator.last_answer)
