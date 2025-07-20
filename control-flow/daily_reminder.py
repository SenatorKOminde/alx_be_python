# control-flow/daily_reminder.py

# Step 1: Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Generate reminder using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Step 3: Add time-sensitivity detail
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    reminder += ". Consider completing it when you have free time."

# Step 4: Print final reminder
print(reminder)
