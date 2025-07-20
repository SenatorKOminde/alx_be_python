# daily_reminder.py

def main():
    # Step 1: Prompt user for input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process the task based on priority using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = f"'{task}' has an unknown priority level."

    # Step 3: Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    # Step 4: Provide the final customized reminder
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()