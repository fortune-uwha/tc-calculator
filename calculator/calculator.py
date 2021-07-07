class Calculator:
    """Calculator to perform these actions: addition / subtraction,
       multiplication / division, take (n) root of number, reset memory and
       default value set to 0.

    """

    def __init__(self, last_answer: float = 0.0) -> None:
        self._last_answer = last_answer

    def verify_input(self, number) -> float:
        """Verify user's input as number."""
        try:
            float(number)
        except ValueError as error:
            raise ValueError(
                "This is not a number. Please enter a valid number.")from None

    @property
    def last_answer(self):
        """Return last value in memory."""
        return self._last_answer

    def add(self, number: float) -> float:
        """Add given number to value in memory."""
        self.verify_input(number)
        self._last_answer += number
        return self._last_answer

    def subtract(self, number: float) -> float:
        """Subtract given number from value in memory."""
        self.verify_input(number)
        self._last_answer -= number
        return self._last_answer

    def multiply(self, number: float) -> float:
        """Multiply given number by value in memory."""
        self.verify_input(number)
        self._last_answer *= number
        return self._last_answer

    def divide(self, number: float) -> float:
        """Divide given number by value in memory."""
        self.verify_input(number)
        try:
            self._last_answer /= number
            return self._last_answer
        except ZeroDivisionError as zd:
            raise ZeroDivisionError(f"You cannot divide by zero! --> {zd}")from None

    def nroot(self, root: float) -> float:
        """Calculate nth root of number in memory."""
        self.verify_input(root)
        if self._last_answer < 0:
            raise ValueError(
                "Calculator cannot take nth root of a negative number.")from None
        try:
            self._last_answer **= (1 / root)
            return self._last_answer
        except ZeroDivisionError as zd:
            raise ZeroDivisionError(
                f"Please provide a non-zero number! --> {zd}")from None

    def reset_memory(self) -> float:
        """Reset default memory value to 0."""
        self._last_answer = 0.0
        return self._last_answer
