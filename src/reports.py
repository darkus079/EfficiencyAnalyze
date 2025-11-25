from abc import ABC, abstractmethod
from collections import defaultdict

from src.models import Employee


class BaseReport(ABC):
    @abstractmethod
    def generate(self, employees: list[Employee]) -> list[tuple]:
        pass

    @abstractmethod
    def get_headers(self) -> list[str]:
        pass


class PerformanceReport(BaseReport):
    def generate(self, employees: list[Employee]) -> list[tuple]:
        position_performances: dict[str, list[float]] = defaultdict(list)

        for employee in employees:
            position_performances[employee.position].append(employee.performance)

        result = []
        for position, performances in position_performances.items():
            avg_performance = sum(performances) / len(performances)
            result.append((position, round(avg_performance, 2)))

        result.sort(key=lambda x: (-x[1], x[0]))

        return [(i + 1, pos, perf) for i, (pos, perf) in enumerate(result)]

    def get_headers(self) -> list[str]:
        return ["#", "Position", "Avg Performance"]

