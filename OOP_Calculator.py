class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        else:
            return self.num1 / self.num2

print("Choose an option:")
print("Type 1 for add")
print("Type 2 for subtract")
print("Type 3 for multiply")
print("Type 4 for divide")

while True:
    choice = int(input("Enter a choice (1-4): "))
    if 1 <= choice <= 4:
        break
    else:
        print("Enter a valid option bro")

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

calc = Calculator(num1, num2)

if choice == 1:
    result = calc.add()
elif choice == 2:
    result = calc.subtract()
elif choice == 3:
    result = calc.multiply()
elif choice == 4:
    result = calc.divide()

print("The result is:", result)