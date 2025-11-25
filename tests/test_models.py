from src.models import Employee


class TestEmployee:
    def test_create_employee(self):
        employee = Employee(
            name="Alex Ivanov",
            position="Backend Developer",
            completed_tasks=45,
            performance=4.8,
            skills="Python, Django",
            team="API Team",
            experience_years=5,
        )

        assert employee.name == "Alex Ivanov"
        assert employee.position == "Backend Developer"
        assert employee.completed_tasks == 45
        assert employee.performance == 4.8
        assert employee.skills == "Python, Django"
        assert employee.team == "API Team"
        assert employee.experience_years == 5

    def test_employee_equality(self):
        employee1 = Employee(
            name="Alex",
            position="Dev",
            completed_tasks=10,
            performance=4.5,
            skills="Python",
            team="Team A",
            experience_years=3,
        )
        employee2 = Employee(
            name="Alex",
            position="Dev",
            completed_tasks=10,
            performance=4.5,
            skills="Python",
            team="Team A",
            experience_years=3,
        )

        assert employee1 == employee2

    def test_employee_inequality(self):
        employee1 = Employee(
            name="Alex",
            position="Dev",
            completed_tasks=10,
            performance=4.5,
            skills="Python",
            team="Team A",
            experience_years=3,
        )
        employee2 = Employee(
            name="Alex",
            position="Dev",
            completed_tasks=11,
            performance=4.5,
            skills="Python",
            team="Team A",
            experience_years=3,
        )

        assert employee1 != employee2

    def test_employee_hashable(self):
        employee = Employee(
            name="Alex",
            position="Dev",
            completed_tasks=10,
            performance=4.5,
            skills="Python",
            team="Team A",
            experience_years=3,
        )

        employees_set = {employee}
        assert employee in employees_set

