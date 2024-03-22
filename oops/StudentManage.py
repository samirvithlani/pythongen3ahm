class StudentDetail:
    
    def __init__(self):
        self.name = ""
        self.age = 0
        self.marks = 0




class Student(StudentDetail):
    
    def __init__(self):
        super().__init__()
        self.student_list = []
        self.student_dict = {}
    
    
    def addStudent(self):
        self.name  = input("Enter Student Name: ")
        self.age = int(input("Enter Student Age: "))
        self.marks = int(input("Enter Student Marks: "))    
        
        self.student_dict = {"Name": self.name, "Age": self.age, "Marks": self.marks}
        self.student_list.append(self.student_dict)
    
    def getAllStudentDetail(self):
        print("Student Detail")
        for i in self.student_list:
            for k,v in i.items():
                print(k,":",v)
    
    def removeStudent(self,name):            
        for i in self.student_list:
            if i["Name"] == name:
                self.student_list.remove(i)
                print("Student Removed Successfully")
    
    def updateStudent(self,name):
        for i in self.student_list:
            if i["Name"] == name:
                self.student_list.remove(i)
                self.name  = input("Enter Student Name to update: ")
                self.age = int(input("Enter Student Age to update: "))
                self.marks = int(input("Enter Student Marks to update: "))
                
                self.student_dict = {"Name": self.name, "Age": self.age, "Marks": self.marks}
                self.student_list.append(self.student_dict)
                print("Student Updated Successfully")
                
                
            else:
                print("Student Not Found")
        
    def getStudentByName(self,name):
       
       if len(self.student_list>0):     
            for i in self.student_list:
                if i["Name"] == name:
                    print("Student Detail")
                    print(i)
                else:
                    print("Student Not Found")            
       else:
           print("No Student Found")            
                
                            
                
                


s = Student()
while True:
    print("1. Add Student")
    print("2. Get All Student Detail")
    print("3. Remove Student")
    print("4. Update Student")
    print("5. Exit")
    print("Enter Your Choice: ")
    choice = int(input())
    match choice:
        case 1:
            s.addStudent()
        case 2:
            s.getAllStudentDetail()
        case 3:
            name = input("Enter Student Name: ")
            s.removeStudent(name)
        case 4:
            name = input("Enter Student Name: ")
            s.updateStudent(name)
        case 5:
            break
            
        
        case _:
            print("Invalid Choice")
                    




                

        