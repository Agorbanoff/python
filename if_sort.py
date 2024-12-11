myList = []
size = int(input("Enter the size of the array \n"))
is_sorted = False  

def entering_array(size):
    for i in range(size):
        number = int(input("Enter a number for the array \n"))
        myList.append(number)

def check_array(array):
    global is_sorted  
    for i in range(size - 1):
        if myList[i] > myList[i+1]:
            is_sorted = True
            break

def check_bool():
    global is_sorted 
    if not is_sorted:  
        print("The array is sorted properly")
    else:
        print("The array is not sorted properly")

entering_array(size)
check_array(myList)
check_bool()
