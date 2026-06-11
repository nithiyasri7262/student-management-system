import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    student = {
        "roll": roll,
        "name": name,
        "department": dept
    }

    students.append(student)
    save_students(students)
    print("Student Added Successfully!")

def view_students(students):
    if not students:
        print("No Records Found")
        return

    print("\nStudent Records")
    for student in students:
        print(student)

def search_student(students):
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student Not Found")

def update_student(students):
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("New Name: ")
            student["department"] = input("New Department: ")

            save_students(students)

            print("Student Updated Successfully!")
            return

    print("Student Not Found")

def delete_student(students):
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)

            save_students(students)

            print("Student Deleted Successfully!")
            return

    print("Student Not Found")

students = load_students()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
