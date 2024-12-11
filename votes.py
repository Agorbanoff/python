age = int(input("Enter you age: \n"))
  
def check_age(age):
    if (age >= 18):
        print("You can vote")
    else:
        print ("you cannot vote")

check_age(age)