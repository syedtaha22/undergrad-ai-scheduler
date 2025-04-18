import os 
import sys

#sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_models.course import Course  # assuming your class is saved in course.py

def run_tests():
    # Create course instances
    course1 = Course(
        name="Data Structures",
        program="BSCS",
        instructor="Dr. Smith",
        id="CS101-A",
        room="Room 101",
        day="Monday",
        time="09:00-10:30",
        comments="Core course"
    )

    course2 = Course(
        name="Operating Systems",
        program="BSCS",
        instructor="Dr. Doe",
        id="CS102-A",
        room="Room 102",
        day="Monday",
        time="10:00-11:30",
        comments="Elective course"
    )

    course3 = Course(
        name="Marketing 101",
        program="BBA",
        instructor="Prof. Jane",
        id="MK201-B",
        room="Room 201",
        day="Tuesday",
        time="09:00-10:30",
        comments=""
    )

    # Test __str__()
    print("Testing __str__:")
    print(course1)
    print()

    # Test clashes_with()
    print("Testing clashes_with:")
    print(f"course1 clashes with course2? {course1.clashes_with(course2)}")  # True (overlap)
    print(f"course1 clashes with course3? {course1.clashes_with(course3)}")  # False (different day)
    print()

    # Test sorting (__lt__)
    print("Testing sorting:")
    course_list = [course2, course1, course3]
    course_list.sort()
    for c in course_list:
        print(c.id)
    print()

    # Test equality (__eq__)
    print("Testing equality:")
    course_duplicate = Course(
        name="Data Structures",
        program="BSCS",
        instructor="Dr. Smith",
        id="CS101-A",  # same ID as course1
        room="Room 999",
        day="Friday",
        time="15:00-16:00",
        comments="Duplicate for test"
    )
    print(f"course1 == course_duplicate? {course1 == course_duplicate}")  # True
    print(f"course1 == course2? {course1 == course2}")  # False

if __name__ == "__main__":
    run_tests()
