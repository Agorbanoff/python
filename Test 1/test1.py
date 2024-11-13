input_string = input("Enter a list of numbers separated by spaces: ")
numbers = [int(number) for number in input_string.split()]
largest_odd = None

for number in numbers:
  
    if number % 2 != 0 and (largest_odd is None or number > largest_odd):
        largest_odd = number


if largest_odd is None:
    print("There are no odd numbers")
else:
    print(f"The largest odd number is: {largest_odd}")
