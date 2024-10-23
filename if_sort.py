myList = []
size = int(input("Enter the size of the array \n"))
bool = False

for i in range(size):
    number = int(input("Enter a number for the array \n"))
    myList.append(number)

for i in range(size - 1):
    if myList[i] > myList[i+1]:
        bool = True
        break

if bool != True:
    print("The array is sorted properly")
else:
    print("The array is not sorted properly")