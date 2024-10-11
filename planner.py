import json
import os
from datetime import datetime
import time
from stringcolor import cs

WORKOUT_FILE = "workout_planner.json"
REPORT_FILE = "workout_report.json"
CAL_BURN_PERMIN = {"easy": 1.6, "medium": 2.1, "hard": 2.5}


class WorkoutNotFoundError(Exception):  # custom exception
    pass


class InvalidInputError(Exception):
    pass


class WorkoutPlanner:
    def __init__(self):
        self.workouts = self.load_workouts()

    def load_workouts(self):
        if os.path.exists(WORKOUT_FILE):
            with open(WORKOUT_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_workouts(self):
        with open(WORKOUT_FILE, "w") as file:
            json.dump(self.workouts, file, indent=4)  # dump is write

    def add_workouts(self, name, duration, difficulty):
        if name in self.workouts:
            raise InvalidInputError(f"Workout '{name}' already exists.")
        self.workouts[name] = {"duration": duration, "difficulty": difficulty}
        time.sleep(0.5)
        self.save_workouts()
        print(f"Added workout: {name}")

    def view_workouts(self):
        if not self.workouts:
            print(cs("No workouts found get up and do something", "red"))
        else:
            for name, details in self.workouts.items():
                print(
                    f"Workout : {name}, Duration : {details['duration']}, Difficulty {details['difficulty']}"
                )
                time.sleep(0.2)

    def update_workout(self, name, duration=None, difficulty=None):
        if name not in self.workouts:
            raise WorkoutNotFoundError(f"Workout {name} not found.")
        if duration:
            self.workouts[name]["duration"] = duration
        if difficulty:
            self.workouts[name]["difficulty"] = difficulty
        self.save_workouts()
        time.sleep(0.5)
        print(cs(f"Updated workout: {name}", "green"))

    def delete_workout(self, name):
        if name not in self.workouts:
            raise WorkoutNotFoundError(f"Workout {name} not found.")
        del self.workouts[name]
        self.save_workouts()
        time.sleep(0.5)
        print(cs(f"Deleted workout: {name}", "yellow"))

    def calculate_calories(self, duration, difficulty):
        return round(duration * CAL_BURN_PERMIN[difficulty])

    def generate_report(self):
        if not self.workouts:
            raise WorkoutNotFoundError(cs("There is no exercises to generate report.", "red"))
        else:
            report = {}
            report["date"] = datetime.now().strftime("%d-%m-%Y")
            report["total_calories"] = 0
            report["total_duration"] = 0
            report["exercises"] = []
            for name, details in self.workouts.items():
                exercise = {
                    "name": name,
                    "duration": details["duration"],
                    "difficulty": details["difficulty"],
                    "calories": self.calculate_calories(details["duration"], details["difficulty"]),
                }
                report["exercises"].append(exercise)
                report["total_duration"] += details["duration"]
                report["total_calories"] += exercise["calories"]
            return report

    def save_report(self):
        if os.path.exists(REPORT_FILE):
            with open(REPORT_FILE, "r") as file:
                existing_reports = json.load(file)
        else:
            existing_reports = []
        existing_reports.append(self.generate_report())
        with open(REPORT_FILE, "w") as file:
            json.dump(existing_reports, file, indent=4)
        time.sleep(0.5)
        print(cs(f"Report for {datetime.now().strftime("%d-%m-%Y")} successfully generated","green",))
