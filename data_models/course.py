

class Course:
    """
    Represents a university course with scheduling information.

    Attributes
    ----------
    name : str
        Name of the course.
    program : str
        Academic program offering the course (e.g., BSCS, BBA).
    instructor : str
        Name of the instructor teaching the course.
    id : str
        Unique identifier for the course section.
    room : str
        Room where the course is held.
    day : str
        Day of the week when the course is scheduled.
    time : str
        Time slot for the course in "HH:MM-HH:MM" format.
    comments : str
        Additional remarks or comments about the course.
    """

    def __init__(self, 
                 name: str, 
                 program: str, 
                 instructor: str, 
                 id: str, 
                 room: str, 
                 day: str, 
                 time: str, 
                 comments: str) -> None:
        self.name = name
        self.program = program
        self.instructor = instructor
        self.id = id
        self.room = room
        self.day = day
        self.time = time
        self.comments = comments

    def __str__(self) -> str:
        """Return a human-readable representation of the course."""
        return (f"{self.time} | {self.name} | {self.program} | {self.room} | "
                f"{self.id} | {self.instructor} | {self.day} | {self.comments}")

    def clashes_with(self, other: 'Course') -> bool:
        """
        Determines whether this course conflicts with another course based on
        overlapping time slots on the same day.

        Parameters
        ----------
        other : Course
            Another course instance to compare with.

        Returns
        -------
        bool
            True if both courses occur on the same day and their time intervals overlap, False otherwise.
        """
        if self.day != other.day:
            return False

        start1, end1 = self._parse_time(self.time)
        start2, end2 = self._parse_time(other.time)

        return start1 < end2 and start2 < end1

    def _parse_time(self, time_str: str) -> tuple[int, int]:
        """
        Parses a time string in "HH:MM-HH:MM" format into integer values.

        Parameters
        ----------
        time_str : str
            Time string representing a time interval.

        Returns
        -------
        tuple[int, int]
            A tuple containing start and end times as integers in HHMM format.
        """
        start_str, end_str = time_str.split("-")
        start = int(start_str.replace(":", ""))
        end = int(end_str.replace(":", ""))
        return start, end

    def __lt__(self, other: 'Course') -> bool:
        """
        Compares two courses by their IDs to support sorting.

        Parameters
        ----------
        other : Course
            Another course instance to compare with.

        Returns
        -------
        bool
            True if this course's ID is less than the other course's ID.
        """
        return self.id < other.id

    def __eq__(self, other: object) -> bool:
        """
        Checks equality of two course instances by their IDs.

        Parameters
        ----------
        other : object
            Another object to compare.

        Returns
        -------
        bool
            True if `other` is a Course with the same ID, False otherwise.
        """
        if not isinstance(other, Course):
            return NotImplemented
        return self.id == other.id