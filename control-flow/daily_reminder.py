# control-flow/daily_reminder.py

# Step 1: Get task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Build base reminder
match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        if time_bound == "yes":
            message = f"Note: '{task}' is a low priority task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Reminder: '{task}' has an unknown priority level."

# Step 3: Print the customized reminder
print(message)
