class Student:
    def setName(self,__name):
        if  user == "teacher":
            self.__name=__name
    def getName(self):
        if user == "teacher":
            return(self.__name)
        else:
            print("Unauthorized User to Enter Name")
    def setRollNumber(self,__rollnum):
        if user == "teacher":
            self.__rollnum=__rollnum
    def getRollNumber(self):
        if user == "teacher":
            return(self.__rollnum)
        else:
            print("Unauthorized User to Enter Roll Number")
user=input("Enter User Name : ") #enter user name "teacher"
a=input("Enter Student name : ")   
b=input("Enter Student Roll Number : ") 
obj=Student()
obj.setName(a)
n=obj.getName()
obj.setRollNumber(b)
r=obj.getRollNumber()
print(f"Name = {n} , RollNumber = {r}\n")

print("Output for wrong user name : ")
user="student"
obj1=Student()
obj1.setName("rahul")
n1=obj1.getName()
obj1.setRollNumber(621456)
r1=obj.getRollNumber()

print(f"Name = {n1} , RollNumber = {r1}")