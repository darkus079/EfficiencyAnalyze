import argparse
import sys

from tabulate import tabulate

from src.factory import ReportFactory
from src.readers import read_multiple_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Developer efficiency analysis tool"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files with employee data",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report type to generate",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        report = ReportFactory.get_report(args.report)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    try:
        employees = read_multiple_files(args.files)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not employees:
        print("No data found in the provided files.", file=sys.stderr)
        return 1

    result = report.generate(employees)
    headers = report.get_headers()

    print(tabulate(result, headers=headers, tablefmt="simple"))

    return 0


if __name__ == "__main__":
    sys.exit(main())

