import pytest

from src.factory import ReportFactory
from src.reports import BaseReport, PerformanceReport


class TestReportFactory:
    def test_get_performance_report(self):
        report = ReportFactory.get_report("performance")

        assert isinstance(report, PerformanceReport)

    def test_get_report_case_insensitive(self):
        report1 = ReportFactory.get_report("PERFORMANCE")
        report2 = ReportFactory.get_report("Performance")
        report3 = ReportFactory.get_report("pErFoRmAnCe")

        assert isinstance(report1, PerformanceReport)
        assert isinstance(report2, PerformanceReport)
        assert isinstance(report3, PerformanceReport)

    def test_get_unknown_report(self):
        with pytest.raises(ValueError) as exc_info:
            ReportFactory.get_report("unknown")

        assert "Unknown report: unknown" in str(exc_info.value)
        assert "Available reports:" in str(exc_info.value)

    def test_get_available_reports(self):
        available = ReportFactory.get_available_reports()

        assert "performance" in available

    def test_register_custom_report(self):
        class CustomReport(BaseReport):
            def generate(self, employees):
                return []

            def get_headers(self):
                return ["Custom"]

        ReportFactory.register_report("custom", CustomReport)

        report = ReportFactory.get_report("custom")
        assert isinstance(report, CustomReport)

        del ReportFactory._reports["custom"]

