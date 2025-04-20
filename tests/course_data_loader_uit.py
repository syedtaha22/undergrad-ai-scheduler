import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_models.course_data_loader import CourseDataLoader


file = "configs/courses.json"

loader = CourseDataLoader(file)

loader.display_schedule()