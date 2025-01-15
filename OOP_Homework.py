class Organization:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.employees = []
    
    def people(self, size):
        while len(self.employees) < size:   
            names = str(input("Enter name: "))
            self.employees.append(names)
        print("Your employees are:")    
        print(self.employees)

    def average_salary(self, salary):
        self.salary = salary
        print(salary)
        print("is the amount of money the employee receives. \n")

    def add_employee(self, employee):
        self.employees.append(employee)
        self.size += 1


class Employee(Organization):
    def __init__(self, name, salary, age):
        super().__init__(name, salary)
        self.salary = salary
        self.age = age

    def decrease_salary(self, amount):
        self.salary -= amount
        print("The new salary is: ")
        print(self.salary)

    def increase_salary(self, amount):
        self.salary += amount
        print("The new salary is: ")
        print(self.salary)


print("Welcome to out organization \n")

size = int(input("Tell us how many people you want our organization to be? \n"))
people_list = Organization(size)
people_list.people(size)

name = str(input("Tell the name of an employee who you want to add more info for \n"))
salary = int(input("Tell us how much you want he/she to earn monthly. \n"))
age = int(input("How old is your employee? \n"))

print("Type 1 if you want to increase the salary of the employee")
print("Type 2 if you want to decrease the salary of the employee")
print("Type 3 if you dont wanna change the salary of the employee")

while True:
    choice = int(input())
    if choice == 1 or choice == 2 or choice == 3:
        break
    else:
        print("Enter a valid option!")

if choice == 1 or choice == 2:
    while True:
        amount = int(input("Enter the amount of money now. \n"))
        if amount <= 0:
            print("Enter an amount bigger than zero! \n")
        else:
            break

employee = Employee(name, salary, age)
employee.average_salary(salary)
employee.add_employee(employee)

if choice == 1:
    employee.increase_salary(amount)
elif choice == 2:
    employee.decrease_salary(amount)

print("\n")
print("------------------------------")
print("The name of the employee is:")
print(employee.name)
print("The employee's age is:")
print(employee.age)
print(employee.salary, "$ is the salary of the employee")
print("------------------------------")