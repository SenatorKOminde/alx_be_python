# daily_reminder.py

# Prompt for user input
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Match Case to determine priority-based reminder
match priority:
    case "high":
        reminder = f"🔔 Task: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"📌 Task: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"📝 Task: '{task}' is a LOW priority task."
    case _:
        reminder = f"⚠️ Task: '{task}' has an UNKNOWN priority level."

# If statement to check if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Final customized output
print(reminder)
