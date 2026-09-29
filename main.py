# Student Grade Management System

students = {}


def add_student():
    """Add a student and their marks."""
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))

    students[name] = marks
    print(f"{name} added successfully!\n")


def view_students():
    """Show all students and their marks."""
    if not students:
        print("No students added yet!\n")
        return

    print("\n--- All Students ---")
    for name, marks in students.items():
        print(f"{name}: {marks} marks")
    print()


def calculate_grade(marks):
    """Return the grade based on marks."""
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"


def show_statistics():
    """Show basic class statistics."""
    if not students:
        print("No students to calculate statistics!\n")
        return

    total = sum(students.values())
    average = total / len(students)

    print("\n--- Class Statistics ---")
    print(f"Total Students: {len(students)}")
    print(f"Average Marks: {average:.2f}")
    print()


def main():
    while True:
        print("=== Student Grade Management ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Grade for Student")
        print("4. Show Statistics")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Enter student name: ")

            if name in students:
                marks = students[name]
                grade = calculate_grade(marks)
                print(f"{name} got {marks} marks - Grade: {grade}\n")
            else:
                print("Student not found!\n")

        elif choice == "4":
            show_statistics()

        elif choice == "5":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
