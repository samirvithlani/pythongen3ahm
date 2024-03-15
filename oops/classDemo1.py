class Student:
    
    name = "amit"
    def getStudentData(self):
         print("Get student Data")
         print("self...",self)
    
    def printStudentName(self,name,age):
        print("Name is ",name)
        print("Age is ",age)     



stu = Student() # creating object of class Student
print(stu.name)     
stu.getStudentData()
print(stu)
stu.printStudentName("Amit",30)
#stu.getStudentData(stu)
#print(name)