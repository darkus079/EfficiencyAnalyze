# EfficiencyAnalyze

Инструмент для анализа эффективности работы разработчиков.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python main.py --files employees1.csv employees2.csv --report performance
```

## Добавление нового отчета

1. Создайте класс-наследник `BaseReport` в `src/reports.py`:

```python
class NewReport(BaseReport):
    def generate(self, employees: list[Employee]) -> list[tuple]:
        # логика формирования отчета
        pass

    def get_headers(self) -> list[str]:
        return ["Header1", "Header2"]
```

2. Зарегистрируйте отчет в `src/factory.py`:

```python
_reports: dict[str, type[BaseReport]] = {
    "performance": PerformanceReport,
    "new_report": NewReport,
}
```
