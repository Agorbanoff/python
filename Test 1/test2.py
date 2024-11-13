my_list = []
size = int(input("Enter the size of the array: "))
boolean = False

for i in range(size):
    number = int(input("Enter a number for the array: "))
    my_list.append(number)

for i in range(size - 1):
    if my_list[i] > my_list[i+1]:
        boolean = True
        print("Масивът не е строго определен")
        breax

if boolean == False:
    print("Масивът е строго определен")