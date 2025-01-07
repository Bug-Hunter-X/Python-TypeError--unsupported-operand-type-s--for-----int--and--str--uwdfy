def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)):
          if b == 0:
            raise ZeroDivisionError("Division by zero")
          result = a / b
          return result
        else:
          raise TypeError("Unsupported operand type(s) for / ")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_uncommon_error(10, "hello")  # Output: Error: Unsupported operand type(s) for /, None
result4 = function_with_uncommon_error(10, 2.5) # Output: 4.0
print(result1, result2, result3, result4)