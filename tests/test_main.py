import pytest
import sys
from io import StringIO

from main import main, parse_args


class TestParseArgs:
    def test_parse_args_single_file(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv", ["main.py", "--files", "file.csv", "--report", "performance"]
        )

        args = parse_args()

        assert args.files == ["file.csv"]
        assert args.report == "performance"

    def test_parse_args_multiple_files(self, monkeypatch):
        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", "file1.csv", "file2.csv", "--report", "performance"],
        )

        args = parse_args()

        assert args.files == ["file1.csv", "file2.csv"]
        assert args.report == "performance"

    def test_parse_args_missing_files(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["main.py", "--report", "performance"])

        with pytest.raises(SystemExit):
            parse_args()

    def test_parse_args_missing_report(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["main.py", "--files", "file.csv"])

        with pytest.raises(SystemExit):
            parse_args()


class TestMain:
    def test_main_success(self, temp_dir, monkeypatch, capsys):
        content = """name,position,completed_tasks,performance,skills,team,experience_years
Alex,Backend Developer,45,4.8,Python,API Team,5
Maria,Frontend Developer,38,4.7,React,Web Team,4"""

        file_path = temp_dir / "employees.csv"
        file_path.write_text(content, encoding="utf-8")

        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", str(file_path), "--report", "performance"],
        )

        result = main()
        captured = capsys.readouterr()

        assert result == 0
        assert "Backend Developer" in captured.out
        assert "Frontend Developer" in captured.out
        assert "4.8" in captured.out
        assert "4.7" in captured.out

    def test_main_unknown_report(self, temp_dir, monkeypatch, capsys):
        content = """name,position,completed_tasks,performance,skills,team,experience_years
Alex,Backend Developer,45,4.8,Python,API Team,5"""

        file_path = temp_dir / "employees.csv"
        file_path.write_text(content, encoding="utf-8")

        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", str(file_path), "--report", "unknown"],
        )

        result = main()
        captured = capsys.readouterr()

        assert result == 1
        assert "Unknown report" in captured.err

    def test_main_file_not_found(self, temp_dir, monkeypatch, capsys):
        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", str(temp_dir / "nonexistent.csv"), "--report", "performance"],
        )

        result = main()
        captured = capsys.readouterr()

        assert result == 1
        assert "File not found" in captured.err

    def test_main_empty_files(self, temp_dir, monkeypatch, capsys):
        file_path = temp_dir / "empty.csv"
        file_path.write_text("", encoding="utf-8")

        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", str(file_path), "--report", "performance"],
        )

        result = main()
        captured = capsys.readouterr()

        assert result == 1
        assert "No data found" in captured.err

    def test_main_multiple_files(self, temp_dir, monkeypatch, capsys):
        content1 = """name,position,completed_tasks,performance,skills,team,experience_years
Alex,Backend Developer,45,4.8,Python,API Team,5"""

        content2 = """name,position,completed_tasks,performance,skills,team,experience_years
Maria,Backend Developer,38,4.6,Python,API Team,4"""

        file1 = temp_dir / "file1.csv"
        file2 = temp_dir / "file2.csv"
        file1.write_text(content1, encoding="utf-8")
        file2.write_text(content2, encoding="utf-8")

        monkeypatch.setattr(
            sys,
            "argv",
            ["main.py", "--files", str(file1), str(file2), "--report", "performance"],
        )

        result = main()
        captured = capsys.readouterr()

        assert result == 0
        assert "Backend Developer" in captured.out
        assert "4.7" in captured.out

