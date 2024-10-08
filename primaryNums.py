
for i in range(2, 1000):
    prime = True
    for k in range(2, i):
        if i % k == 0:
            prime = False
    if prime:
        print(i, " is prime")



# броячите автоматично се увеличават с 1