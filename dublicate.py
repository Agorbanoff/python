myList = []
size = int(input("Enter the size of the array \n"))

def entering_array(size, myList):
    for i in range(size):
        number = int(input("Enter a number for the array \n"))
        myList.append(number)

def removing_duplicates(myList):
    for i in range(size - 2):
        if myList[i] == myList[i + 1]:
            myList.pop(i+1)
    print(myList)

entering_array(size, myList)
removing_duplicates(myList)
