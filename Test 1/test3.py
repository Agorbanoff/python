my_list = []  
size = int(input("Enter the size of the array: "))
seen = []
for i in range(size):
    number = int(input("Enter a number for the array: "))
    if number not in seen:
        seen.append(number)
        my_list.append(number)


my_list.reverse()  

print("The unique numbers in the array in reversed order are: \n")
for number in my_list:
    print(number)
