from student_manager import (
    display_record,
    search_student,
    add_student,
    update_marks,
    display_all_students
)
from data_store import students

def main_menu():
    """Sub-menu interface."""
    while True:
        print("\n========================")
        print("        MAIN MENU       ")
        print("========================")
        print("1. Search Student")
        print("2. Add Student Data")
        print("3. Update Student Marks")
        print("4. Display All Students")
        print("5. Back to Main Screen")

        choice = input("\nEnter choice (1-5): ")
        if choice == "1":
            search_student()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please try again.")

def main():
    """Main program execution loop."""
    while True:
        print("\n=====================================")
        print("     STUDENT RECORD MANAGEMENT       ")
        print("=====================================")
        print("Options: [Student ID] | 'NEW' | 'MENU' | 'EXIT'")
        
        user_input = input("\nEnter choice: ").upper()

        if user_input in students:
            display_record(user_input)
        elif user_input == "NEW":
            add_student()
        elif user_input == "MENU":
            main_menu()
        elif user_input == "EXIT":
            print("\nThank you for using Student Record Management System!")
            break
        else:
            print("\nID not found or invalid command. Type MENU for options.")

if __name__ == "__main__":
    main()