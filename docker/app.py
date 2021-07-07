from calculator.calculator import Calculator

calculator = Calculator()

result = calculator.add(10)
print(f"0+4 = {result}")

result = calculator.subtract(3)
print(f"value_in_memory - 3 = {result}")

result = calculator.divide(7)
print(f"value_in_memory - 3 = {result}")

calculator.add(26)
result = calculator.nroot(3)
print(f"cube root of value_in_memory = {result}")

calculator.reset_memory()
