import math
class student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.grade = 1 

    def upgrade(self):
        self.grade += 1

stud1 = student(1,"Pavel")
stud2 = student(2,"Hela")
stud3 = student(3,"Rostik")

students = [stud1,stud2,stud3]

## projdi všechny studenty a vypiš jejich jména a roční
for stu in students: 
    print("Name: ",stu.name,"\tRočník: ",stu.grade)

## projdi poslední dva studenty a vypiš jejich jména
for stu in students[-2:]: 
    print(stu.name,math.pi)


