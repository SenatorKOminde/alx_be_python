def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for non-numeric input and division by zero.

    :param numerator: The numerator (as a string or number)
    :param denominator: The denominator (as a string or number)
    :return: A string message with result or appropriate error
    """
    try:
        # Convert inputs to float (handles string representations of numbers)
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result:.1f}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."