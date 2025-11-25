import pytest
from pathlib import Path
import tempfile
import os


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_csv_content():
    return """name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django",API Team,5
Maria Petrova,Frontend Developer,38,4.7,"React, TypeScript",Web Team,4
John Smith,Backend Developer,29,4.6,"Python, Flask",API Team,3"""


@pytest.fixture
def sample_csv_file(temp_dir, sample_csv_content):
    file_path = temp_dir / "employees.csv"
    file_path.write_text(sample_csv_content, encoding="utf-8")
    return file_path


@pytest.fixture
def sample_csv_semicolon_content():
    return """name;position;completed_tasks;performance;skills;team;experience_years
Alex Ivanov;Backend Developer;45;4.8;Python, Django;API Team;5
Maria Petrova;Frontend Developer;38;4.7;React, TypeScript;Web Team;4"""


@pytest.fixture
def sample_csv_semicolon_file(temp_dir, sample_csv_semicolon_content):
    file_path = temp_dir / "employees_semicolon.csv"
    file_path.write_text(sample_csv_semicolon_content, encoding="utf-8")
    return file_path


@pytest.fixture
def empty_csv_file(temp_dir):
    file_path = temp_dir / "empty.csv"
    file_path.write_text("", encoding="utf-8")
    return file_path


@pytest.fixture
def headers_only_csv_file(temp_dir):
    file_path = temp_dir / "headers_only.csv"
    file_path.write_text(
        "name,position,completed_tasks,performance,skills,team,experience_years\n",
        encoding="utf-8"
    )
    return file_path

