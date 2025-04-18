import json
from typing import List, Any, Dict
from rich.table import Table
from rich.console import Console

from .course import Course


class CourseDataLoader:
    """
    Loads a JSON file of courses and returns a list of `Course` instances.
    Provides functionality to display the schedule as a timetable using rich tables.

    Attributes
    ----------
    json_path : str
        Path to the JSON file containing course data.
    console : Console
        Rich console object used for rendering the timetable.
    """

    REQUIRED_FIELDS: Dict[str, type] = {
        'name': str,
        'program': str,
        'instructor': str,
        'id': str,
        'room': str,
        'day': str,
        'time': str,
        'comments': str
    }

    def __init__(self, json_path: str) -> None:
        """
        Initializes the data loader with the path to a JSON file.

        Parameters
        ----------
        json_path : str
            Path to the JSON file containing the list of courses.
        """
        self.json_path: str = json_path
        self.console: Console = Console()

    def load_courses(self) -> List[Course]:
        """
        Loads and validates course data from the JSON file.

        Returns
        -------
        List[Course]
            A list of validated Course instances.

        Raises
        ------
        TypeError
            If the JSON root or any item is not of the expected type.
        KeyError
            If a required field is missing in any course entry.
        """
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise TypeError(f"Expected JSON array, got {type(data).__name__}")

        courses: List[Course] = []
        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                raise TypeError(f"Item at index {idx} is not an object: {item}")

            validated: Dict[str, Any] = {}
            for field, field_type in self.REQUIRED_FIELDS.items():
                if field not in item:
                    raise KeyError(f"Missing required field '{field}' in item at index {idx}")
                value = item[field]
                if not isinstance(value, field_type):
                    try:
                        value = field_type(value)  # type: ignore
                    except Exception:
                        raise TypeError(
                            f"Field '{field}' at index {idx} expected {field_type.__name__}, got {type(item[field]).__name__}"
                        )
                validated[field] = value

            course_obj = Course(**validated)
            courses.append(course_obj)

        return courses

    def display_schedule(self) -> None:
        """
        Displays the loaded course schedule in a tabular timetable format using `rich`.

        The timetable groups courses by their time slots (rows) and days (columns).
        If multiple courses occur at the same time on the same day, they are stacked as sub-rows.
        """
        courses: List[Course] = self.load_courses()

        days_order: List[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        days: List[str] = sorted({c.day.strip() for c in courses},
                                 key=lambda d: days_order.index(d) if d in days_order else len(days_order))
        times: List[str] = sorted({c.time for c in courses})

        schedule: Dict[str, Dict[str, List[str]]] = {
            t: {day: [] for day in days} for t in times
        }

        for c in courses:
            schedule[c.time][c.day.strip()].append(c.name)

        table: Table = Table(show_lines=True)
        table.add_column("Time")
        for day in days:
            table.add_column(day)

        for t in times:
            max_rows: int = max(len(schedule[t][day]) for day in days)
            for row_idx in range(max_rows if max_rows > 0 else 1):
                row: List[str] = [t if row_idx == 0 else ""]
                for day in days:
                    courses_list: List[str] = schedule[t][day]
                    cell: str = courses_list[row_idx] if row_idx < len(courses_list) else ""
                    row.append(cell)
                table.add_row(*row)

        self.console.print(table)
