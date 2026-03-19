from datetime import date, timedelta


# Class representing a workout
class Workout:
    def __init__(self, sport, duration):
        self.sport = sport
        self.duration = duration
        self.date = date.today()

    # Method to calculate calories burned for one workout
    def calories(self):
        if self.sport == "running":
            return self.duration * 10
        elif self.sport == "swimming":
            return self.duration * 8
        elif self.sport == "pilates":
            return self.duration * 5
        else:
            return 0


# Save workout to file
def save_workout(workout):
    with open("workouts.txt", "a") as f:
        f.write(f"{workout.sport},{workout.duration},{workout.date}\n")


# Load workouts from file
def load_workouts():
    workouts_list = []
    try:
        with open("workouts.txt", "r") as f:
            for line in f:
                sport, duration, workout_date = line.strip().split(",")
                w = Workout(sport, int(duration))
                w.date = date.fromisoformat(workout_date)
                workouts_list.append(w)
    except FileNotFoundError:
        pass
    return workouts_list


workouts = load_workouts()


# Menu
while True:
    print("\nWhat do you want to do?")
    print("1 - Add workout")
    print("2 - Show workouts")
    print("3 - Show total time (last 7 days)")
    print("4 - Show calories burned (last 7 days)")
    print("Any other number - Exit")

    choice = int(input("Please enter a number: "))

    # Add workout
    if choice == 1:
        sport = input("Sport (running/swimming/pilates): ").lower()
        duration = int(input("Duration in minutes: "))
        w = Workout(sport, duration)
        workouts.append(w)
        save_workout(w)
        print("Workout added on", w.date)

    # Show workouts
    elif choice == 2:
        for w in workouts:
            print(w.date, "-", w.sport, "-", w.duration, "minutes")

    # Calculate total time for the last 7 days
    elif choice == 3:
        total_time = 0
        limit = date.today() - timedelta(days=7)

        for w in workouts:
            if w.date >= limit:
                total_time += w.duration

        print("Total time in the last 7 days:", total_time, "minutes")

    # Calculate calories burned for the last 7 days
    elif choice == 4:
        total_calories = 0
        limit = date.today() - timedelta(days=7)

        for w in workouts:
            if w.date >= limit:
                total_calories += w.calories()

        print("Calories burned in the last 7 days:", total_calories, "kcal")

    # Exit program
    else:
        print("Program ended.")
        break
