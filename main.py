import sys

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id  # Unique employee ID (string or numeric)
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Dept: {self.department} | Salary: {self.salary}"

class EmployeeManagementSystem:
    def __init__(self):
        # Dictionary to store employees with emp_id as key
        self.employees = {}

    def validate_employee_id(self, emp_id):
        """Validates the employee ID.
           - Checks if the ID is numeric.
           - Checks if the ID already exists.
        """
        if not str(emp_id).isdigit():
            print("Error: Employee ID must be numeric.")
            return False
        if emp_id in self.employees:
            print("Error: Employee ID already exists.")
            return False
        return True

    def add_employee(self):
        emp_id = input("Enter Employee ID: ").strip()
        if not self.validate_employee_id(emp_id):
            return
        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        salary_input = input("Enter Salary: ").strip()
        try:
            salary = float(salary_input)
        except ValueError:
            print("Error: Salary must be a number.")
            return

        new_emp = Employee(emp_id, name, department, salary)
        self.employees[emp_id] = new_emp
        print("Employee added successfully.\n")

    def view_employees(self):
        if not self.employees:
            print("No employees found.\n")
            return
        print("Employee List:")
        for emp in self.employees.values():
            print(emp)
        print()

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()
        if emp_id not in self.employees:
            print("Error: Employee not found.\n")
            return
        emp = self.employees[emp_id]
        print("Leave field blank to keep current value.")
        name = input(f"Enter new name [{emp.name}]: ").strip()
        department = input(f"Enter new department [{emp.department}]: ").strip()
        salary_input = input(f"Enter new salary [{emp.salary}]: ").strip()

        if name:
            emp.name = name
        if department:
            emp.department = department
        if salary_input:
            try:
                emp.salary = float(salary_input)
            except ValueError:
                print("Error: Salary must be a number. Keeping old salary.")
        print("Employee updated successfully.\n")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ").strip()
        if emp_id not in self.employees:
            print("Error: Employee not found.\n")
            return
        del self.employees[emp_id]
        print("Employee deleted successfully.\n")

    def search_employee(self):
        print("Search Options:")
        print("1. By Employee ID")
        print("2. By Employee Name")
        choice = input("Choose search option (1/2): ").strip()
        if choice == "1":
            emp_id = input("Enter Employee ID to search: ").strip()
            emp = self.employees.get(emp_id)
            if emp:
                print("Employee found:")
                print(emp)
            else:
                print("Employee not found.")
        elif choice == "2":
            name = input("Enter Employee Name to search: ").strip().lower()
            found = False
            for emp in self.employees.values():
                if name in emp.name.lower():
                    if not found:
                        print("Employee(s) found:")
                    print(emp)
                    found = True
            if not found:
                print("Employee not found.")
        else:
            print("Invalid option selected.")
        print()

    def menu(self):
        while True:
            print("=== Employee Management System ===")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                print("Exiting the Employee Management System.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.\n")

def main():
    system = EmployeeManagementSystem()
    system.menu()

if __name__ == "__main__":
    main()
