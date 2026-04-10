class Student:
    def __init__(self, student_id, name, age, grade, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, "
                f"Grade: {self.grade}, Course: {self.course}")


class StudentRecordSystem:
    def __init__(self):
        self.students = {}

    # Add Student
    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("❌ Student ID already exists!")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        course = input("Enter Course: ")

        self.students[student_id] = Student(student_id, name, age, grade, course)
        print("✅ Student added successfully!")

    # Search Student
    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        student = self.students.get(student_id)

        if student:
            print("🔍 Student Found:")
            print(student)
        else:
            print("❌ Student not found!")

    # Update Student
    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        student = self.students.get(student_id)

        if not student:
            print("❌ Student not found!")
            return

        print("Leave blank to keep existing value")

        name = input(f"Enter Name ({student.name}): ") or student.name
        age_input = input(f"Enter Age ({student.age}): ")
        age = int(age_input) if age_input else student.age
        grade = input(f"Enter Grade ({student.grade}): ") or student.grade
        course = input(f"Enter Course ({student.course}): ") or student.course

        self.students[student_id] = Student(student_id, name, age, grade, course)
        print("✅ Student updated successfully!")

    # Delete Student
    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.students:
            del self.students[student_id]
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found!")

    # Display All Students
    def display_students(self):
        if not self.students:
            print("📭 No student records found!")
            return

        print("\n📚 Student Records:")
        for student in self.students.values():
            print(student)


# Main Menu
def main():
    system = StudentRecordSystem()

    while True:
        print("\n===== Student Record System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.search_student()
        elif choice == '3':
            system.update_student()
        elif choice == '4':
            system.delete_student()
        elif choice == '5':
            system.display_students()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
