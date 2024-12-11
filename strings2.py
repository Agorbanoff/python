my_list = []
size = int(input("Enter the number of words you want in your array:\n"))

def entering_array(my_list):
    for i in range (size):
        words = input("Enter a word for your array: \n")
        my_list.append(words)

def check_largest(size, my_list):
    i = 0
    while i < size:
        biggest = my_list[i]
        k = i + 1
        for k in range(size):
            if len(biggest) < len(my_list[k]):
                biggest = my_list[k]
        i +=1
    print (biggest, "is the largest word in your list")

entering_array(my_list)
check_largest(size, my_list)



