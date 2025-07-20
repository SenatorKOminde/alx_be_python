# control-flow/daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            if priority == "low":
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"Reminder: '{task}' is a {priority} priority task.")
    case _:
        print("Invalid priority level.")
