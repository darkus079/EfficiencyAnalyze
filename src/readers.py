import csv
from pathlib import Path

from src.models import Employee


class CSVReader:
    DELIMITERS = [",", ";", "\t", "|"]

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def _detect_delimiter(self, sample: str) -> str:
        for delimiter in self.DELIMITERS:
            if delimiter in sample:
                return delimiter
        return ","

    def read(self) -> list[Employee]:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            first_line = file.readline()
            if not first_line.strip():
                return []

            delimiter = self._detect_delimiter(first_line)
            file.seek(0)

            reader = csv.DictReader(file, delimiter=delimiter)
            employees = []

            for row in reader:
                employee = Employee(
                    name=row["name"],
                    position=row["position"],
                    completed_tasks=int(row["completed_tasks"]),
                    performance=float(row["performance"]),
                    skills=row["skills"],
                    team=row["team"],
                    experience_years=int(row["experience_years"]),
                )
                employees.append(employee)

            return employees


def read_multiple_files(file_paths: list[str]) -> list[Employee]:
    all_employees: list[Employee] = []

    for file_path in file_paths:
        reader = CSVReader(file_path)
        employees = reader.read()
        all_employees.extend(employees)

    return all_employees

