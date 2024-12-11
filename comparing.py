my_list = ["mitko", "me", "alex", "martin", "skibidi", "sigmarizz", "ohiogodkaicenat"]
n = int(input("Enter n "))
count = int(0)

def count_loop(my_list, count, n): 
    for i in my_list:
        if len(i) >= n:
            count+=1
    print(count)

count_loop(my_list, count, n)




