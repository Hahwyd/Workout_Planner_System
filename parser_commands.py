import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Your new workout planner using CLI")
    subparsers = parser.add_subparsers(dest="command")
    # add workout parser
    add_workout_parser = subparsers.add_parser("add", help="Add new workout")
    add_workout_parser.add_argument("name", type=str)
    add_workout_parser.add_argument("duration", type=int)
    add_workout_parser.add_argument("difficulty", type=str, choices=["easy", "medium", "hard"])
    # view workout parser
    subparsers.add_parser("view", help="View all workouts")
    # update workout parser
    update_parser = subparsers.add_parser("update", help="Update new workout")
    update_parser.add_argument("name", type=str)
    update_parser.add_argument("--duration", type=int)  # --optional
    update_parser.add_argument("--difficulty", type=str, choices=["easy", "medium", "hard"])
    # delete workout parser
    delete_parser = subparsers.add_parser("delete", help="Delete a workout")
    delete_parser.add_argument("name", type=str, help="Name of the workout to delete")
    # generate report parser
    generate_report_parser = subparsers.add_parser("generate", help="Generate report")

    return parser
