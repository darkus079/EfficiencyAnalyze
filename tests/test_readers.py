import pytest

from src.readers import CSVReader, read_multiple_files
from src.models import Employee


class TestCSVReader:
    def test_read_csv_file(self, sample_csv_file):
        reader = CSVReader(str(sample_csv_file))
        employees = reader.read()

        assert len(employees) == 3
        assert all(isinstance(e, Employee) for e in employees)

    def test_read_csv_first_employee(self, sample_csv_file):
        reader = CSVReader(str(sample_csv_file))
        employees = reader.read()

        first = employees[0]
        assert first.name == "Alex Ivanov"
        assert first.position == "Backend Developer"
        assert first.completed_tasks == 45
        assert first.performance == 4.8
        assert first.skills == "Python, Django"
        assert first.team == "API Team"
        assert first.experience_years == 5

    def test_read_csv_with_semicolon_delimiter(self, sample_csv_semicolon_file):
        reader = CSVReader(str(sample_csv_semicolon_file))
        employees = reader.read()

        assert len(employees) == 2
        assert employees[0].name == "Alex Ivanov"
        assert employees[1].name == "Maria Petrova"

    def test_read_nonexistent_file(self, temp_dir):
        reader = CSVReader(str(temp_dir / "nonexistent.csv"))

        with pytest.raises(FileNotFoundError):
            reader.read()

    def test_read_empty_file(self, empty_csv_file):
        reader = CSVReader(str(empty_csv_file))
        employees = reader.read()

        assert employees == []

    def test_read_headers_only_file(self, headers_only_csv_file):
        reader = CSVReader(str(headers_only_csv_file))
        employees = reader.read()

        assert employees == []


class TestReadMultipleFiles:
    def test_read_multiple_files(self, temp_dir):
        content1 = """name,position,completed_tasks,performance,skills,team,experience_years
Alex,Backend Developer,45,4.8,Python,API Team,5"""

        content2 = """name,position,completed_tasks,performance,skills,team,experience_years
Maria,Frontend Developer,38,4.7,React,Web Team,4"""

        file1 = temp_dir / "file1.csv"
        file2 = temp_dir / "file2.csv"
        file1.write_text(content1, encoding="utf-8")
        file2.write_text(content2, encoding="utf-8")

        employees = read_multiple_files([str(file1), str(file2)])

        assert len(employees) == 2
        assert employees[0].name == "Alex"
        assert employees[1].name == "Maria"

    def test_read_multiple_files_with_empty(self, temp_dir, empty_csv_file):
        content = """name,position,completed_tasks,performance,skills,team,experience_years
Alex,Backend Developer,45,4.8,Python,API Team,5"""

        file1 = temp_dir / "file1.csv"
        file1.write_text(content, encoding="utf-8")

        employees = read_multiple_files([str(file1), str(empty_csv_file)])

        assert len(employees) == 1
        assert employees[0].name == "Alex"

    def test_read_multiple_files_nonexistent(self, temp_dir):
        with pytest.raises(FileNotFoundError):
            read_multiple_files([str(temp_dir / "nonexistent.csv")])

