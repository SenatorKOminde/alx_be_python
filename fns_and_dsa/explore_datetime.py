# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return formatted_date

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future)
        return formatted_future
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return None

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()