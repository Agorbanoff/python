grade = input("Type a grade: ")
grade = int(grade)

def check_correct_input(grade):
   while True:
        if   grade > 6 or grade < 2:
            grade = int(input("Type a grade between 2 and 6: "))
        else:
           return False
def check_grade(grade):
    if grade == 2:
        print( "slab")
    elif grade == 3:
        print ("sreden")
    elif grade == 4:
        print ("dobar")
    elif grade == 5:
        print ("mn dobar")
    elif grade == 6:
        print ("otlichen")
    print("your grade is: " +  str(grade))

check_correct_input(grade)
check_grade(grade)
