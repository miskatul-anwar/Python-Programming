def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Attempted to divide by zero.")
        result = a / b
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except TypeError:
        return "Error: Unsupported operand type(s)."
    else:
        if result > 0:
            return f"Result: {result} (positive)"
        elif result < 0:
            return f"Result: {result} (negative)"
        else:
            return "Result: 0 (zero)"


# Test cases
print(divide(10, 2))  # This will print "Result: 5.0 (positive)"
print(divide(10, 0))  # This will print "Error: Attempted to divide by zero."
print(divide(10, "a"))  # This will print "Error: Unsupported operand type(s)."
print(divide(-10, 2))  # This will print "Result: -5.0 (negative)"
print(divide(0, 2))  # This will print "Result: 0 (zero)"
