from src.reports import BaseReport, PerformanceReport


class ReportFactory:
    _reports: dict[str, type[BaseReport]] = {
        "performance": PerformanceReport,
    }

    @classmethod
    def get_report(cls, report_name: str) -> BaseReport:
        report_name_lower = report_name.lower()
        if report_name_lower not in cls._reports:
            available = ", ".join(cls._reports.keys())
            raise ValueError(
                f"Unknown report: {report_name}. Available reports: {available}"
            )
        return cls._reports[report_name_lower]()

    @classmethod
    def register_report(cls, name: str, report_class: type[BaseReport]) -> None:
        cls._reports[name.lower()] = report_class

    @classmethod
    def get_available_reports(cls) -> list[str]:
        return list(cls._reports.keys())

