class Athlete:
    def __init__(self, name, age, weight, height, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.daily_calories_goal = self.calculate_daily_calories_goal()
        self.daily_calories_intake = 0
        self.meals = []

    def calculate_daily_calories_goal(self):
        if self.goal == 'lose':
            return int(self.weight * 25)
        elif self.goal == 'maintain':
            return int(self.weight * 30)
        elif self.goal == 'gain':
            return int(self.weight * 35)

    def display_profile(self):
        print(f"\nAthlete Profile for {self.name}:")
        print(f"Age: {self.age} years")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} cm")
        print(f"Goal: {self.goal} weight")
        print(f"Daily Calories Goal: {self.daily_calories_goal} calories")
        print(f"Daily Calories Intake: {self.daily_calories_intake} calories")
        print("Meals Recorded:")
        for meal in self.meals:
            print(f"{meal['name']}: {meal['calories']} calories")

    def record_meal(self, meal_name, calories):
        self.meals.append({'name': meal_name, 'calories': calories})
        self.daily_calories_intake += calories

    def track_progress(self):
        remaining_calories = self.daily_calories_goal - self.daily_calories_intake
        if remaining_calories > 0:
            return f"Remaining Calories: {remaining_calories} calories"
        elif remaining_calories == 0:
            return "Calorie Goal Achieved"
        else:
            return f"Exceeded Goal by {-remaining_calories} calories"


def main():
    print("Athlete Diet Management System")
    athlete_name = input("Enter your name: ")
    athlete_age = int(input("Enter your age: "))
    athlete_weight = float(input("Enter your current weight (kg): "))
    athlete_height = float(input("Enter your height (cm): "))
    athlete_goal = input("Enter your goal (lose/maintain/gain): ")

    athlete = Athlete(athlete_name, athlete_age, athlete_weight, athlete_height, athlete_goal)

    while True:
        print("\nOptions:")
        print("1. Display Profile")
        print("2. Record Meal")
        print("3. Track Progress")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            athlete.display_profile()
        elif choice == "2":
            meal_name = input("Enter meal name: ")
            calories = float(input("Enter calories consumed: "))
            athlete.record_meal(meal_name, calories)
            print("Meal recorded.")
        elif choice == "3":
            progress = athlete.track_progress()
            print(progress)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


