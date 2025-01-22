class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades 

    def average_grade(self, subject=None):
        if subject:
            if subject in self.grades:
                return sum(self.grades[subject]) / len(self.grades[subject])
            else:
                return f"No grades recorded for {subject}"
        else:
            total_grades = 0
            count_grades = 0
            for grades_list in self.grades.values():
                total_grades += sum(grades_list)
                count_grades += len(grades_list)
            return total_grades / count_grades if count_grades else 0


student = Student("Ivan Ivanov", {"math": [5, 6], "english": [5, 5], "physics": [4, 6]})
print("The average of the grades is: ")
print(student.average_grade())
print("The average grades in math is: ")  
print(student.average_grade("math"))
print("The average grades in english is: ")    
print(student.average_grade("english"))
print("The average grades in physics is: ")    
print(student.average_grade("physics"))    
