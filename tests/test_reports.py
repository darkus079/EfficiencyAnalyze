import pytest

from src.reports import PerformanceReport
from src.models import Employee


class TestPerformanceReport:
    def test_generate_report(self):
        employees = [
            Employee("Alex", "Backend Developer", 45, 4.8, "Python", "Team A", 5),
            Employee("Maria", "Frontend Developer", 38, 4.7, "React", "Team B", 4),
            Employee("John", "Backend Developer", 29, 4.6, "Python", "Team A", 3),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert len(result) == 2
        assert result[0] == (1, "Backend Developer", 4.7)
        assert result[1] == (2, "Frontend Developer", 4.7)

    def test_generate_report_sorting(self):
        employees = [
            Employee("Alex", "Backend Developer", 45, 4.5, "Python", "Team A", 5),
            Employee("Maria", "Frontend Developer", 38, 4.9, "React", "Team B", 4),
            Employee("John", "DevOps Engineer", 29, 4.7, "Docker", "Team C", 3),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert result[0][1] == "Frontend Developer"
        assert result[0][2] == 4.9
        assert result[1][1] == "DevOps Engineer"
        assert result[1][2] == 4.7
        assert result[2][1] == "Backend Developer"
        assert result[2][2] == 4.5

    def test_generate_report_same_performance_alphabetical(self):
        employees = [
            Employee("Alex", "Zebra Developer", 45, 4.5, "Python", "Team A", 5),
            Employee("Maria", "Alpha Developer", 38, 4.5, "React", "Team B", 4),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert result[0][1] == "Alpha Developer"
        assert result[1][1] == "Zebra Developer"

    def test_generate_report_average_calculation(self):
        employees = [
            Employee("Alex", "Backend Developer", 45, 4.0, "Python", "Team A", 5),
            Employee("John", "Backend Developer", 29, 5.0, "Python", "Team A", 3),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert result[0][2] == 4.5

    def test_generate_report_numbering(self):
        employees = [
            Employee("Alex", "Position A", 45, 4.9, "Python", "Team A", 5),
            Employee("Maria", "Position B", 38, 4.8, "React", "Team B", 4),
            Employee("John", "Position C", 29, 4.7, "Docker", "Team C", 3),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert result[0][0] == 1
        assert result[1][0] == 2
        assert result[2][0] == 3

    def test_get_headers(self):
        report = PerformanceReport()
        headers = report.get_headers()

        assert headers == ["#", "Position", "Avg Performance"]

    def test_generate_report_empty_list(self):
        report = PerformanceReport()
        result = report.generate([])

        assert result == []

    def test_generate_report_single_employee(self):
        employees = [
            Employee("Alex", "Backend Developer", 45, 4.8, "Python", "Team A", 5),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert len(result) == 1
        assert result[0] == (1, "Backend Developer", 4.8)

    def test_generate_report_rounding(self):
        employees = [
            Employee("Alex", "Backend Developer", 45, 4.85, "Python", "Team A", 5),
            Employee("John", "Backend Developer", 29, 4.86, "Python", "Team A", 3),
            Employee("Mike", "Backend Developer", 29, 4.87, "Python", "Team A", 3),
        ]

        report = PerformanceReport()
        result = report.generate(employees)

        assert result[0][2] == 4.86

