# ------------------------------------------------- #
# Title: Assignment06.py
# Description: Course Registration Program
# ChangeLog: (Your Name), 02/23/2026, Created Script
# ------------------------------------------------- #

import json
from email import message_from_string

# -------------------- Constants -------------------- #
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

FILE_NAME: str = "Enrollments.json"

# -------------------- Variables -------------------- #
menu_choice: str = ""
students: list = []


# -------------------- Classes -------------------- #

class IO:
    """Performs Input and Output tasks for the Course Registration Program."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays structured error messages."""
        print("\033[1;91mERROR:\033[0m", message)
        if error:
            print("\033[1;91mTechnical Details:\033[0m", error)

    @staticmethod
    def output_menu(menu: str):
        """Displays the program menu."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the user's menu choice."""
        return input("Enter your menu choice [1-4]: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays student enrollment data."""
        print("\nCurrent Enrollment Data:")
        for row in student_data:
            print(f"{row['FirstName']},{row['LastName']},{row['CourseName']}")
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """Collects student enrollment data from the user."""
        try:
            first_name = input("Enter student's first name: ").strip()
            if not first_name.isalpha():
                raise ValueError("\033[1;33mFirst name must contain only letters\033[0m.")

        except Exception as e:
            IO.output_error_messages("\033[1;33mInvalid first name.\033[0m", e)
            return

        try:
            last_name = input("Enter student's last name: ").strip()
            if not last_name.isalpha():
                raise ValueError("\033[1;33mLast name must contain only letters.\033[0m")

        except Exception as e:
            IO.output_error_messages("\033[1;33mInvalid last name.\033[0m", e)
            return

        course_name = input("Enter course name: ").strip()

        student_data.append({
            "FirstName": first_name,
            "LastName": last_name,
            "CourseName": course_name
        })

        print("Student registration added.\n")


class FileProcessor:
    """Processes data to and from a JSON file."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads student enrollment data from a JSON file."""
        try:
            file = open(file_name, "r")
            student_data.clear()
            student_data.extend(json.load(file))
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("\033[1;33mFile not found. Starting with empty list.\033[0m", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("\033[1;33mmFile contains invalid JSON.\033[0m", e)
        except Exception as e:
            IO.output_error_messages("\033[1;33mmUnexpected error while reading file.\033[0m", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student enrollment data to a JSON file."""
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            file.close()
            print("Data successfully saved to file.")
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("\033[91mWarning:Error writing data to file.\033[0m", e)


# -------------------- Main Program -------------------- #

# Load existing data at startup
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    elif menu_choice == "2":
        IO.output_student_courses(students)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    elif menu_choice == "4":
        print("Program ended...Goodbye!")
        break

    else:
        IO.output_error_messages("\033[91mPlease select a valid option (1-4).\033[0m")
