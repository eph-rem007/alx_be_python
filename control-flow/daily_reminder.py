task=input("Enter task: ")
priority= input("Enter its priority. (High, medium, low): ").lower()
time_bound=input("Is the task time bound? (Yes/No): ").lower()
match priority:
    case "high":
        if (time_bound=="yes"):
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif (time_bound=="no"):
            print(f"{task} is a high priority task but you can do it when you have free time")
            