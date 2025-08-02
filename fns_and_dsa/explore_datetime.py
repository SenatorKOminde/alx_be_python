# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

def main():
    print("=== Exploring Python's datetime Module ===\n")
    display_current_datetime()
    print()  # Add a blank line for readability
    calculate_future_date()

if __name__ == "__main__":
    main()
