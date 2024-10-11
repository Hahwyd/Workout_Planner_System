from planner import WorkoutPlanner, InvalidInputError, WorkoutNotFoundError
from parser_commands import create_parser
from stringcolor import cs


def main():
    workout_planner = WorkoutPlanner()
    parser = create_parser()
    # breakpoint()
    args = parser.parse_args()
    try:
        if args.command == "add":
            workout_planner.add_workouts(args.name, args.duration, args.difficulty)
        elif args.command == "view":
            workout_planner.view_workouts()
        elif args.command == "update":
            workout_planner.update_workout(args.name, args.duration, args.difficulty)
        elif args.command == "delete":
            workout_planner.delete_workout(args.name)
        elif args.command == "generate":
            workout_planner.save_report()
        else:
            parser.print_help()

    except (WorkoutNotFoundError, InvalidInputError) as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()
