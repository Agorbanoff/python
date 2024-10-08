grade = input("Type a grade: ")
grade = int(grade)

if grade > 6 or grade < 2:
    grade = input("Type a grade: ")
    grade = int(grade)

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
