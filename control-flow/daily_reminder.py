# daily_reminder.py

# Step 1: Get inputs
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Step 2: Match based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Step 3: Check if task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Step 4: Print the customized reminder
print(reminder)
