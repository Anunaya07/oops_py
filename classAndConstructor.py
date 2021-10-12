class Employee: #class defining
    def __init__(self,fname,lname,salary): #defining constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary

harry=Employee("harry","bhai",34000)
print(harry)
print(harry.fname,harry.lname,harry.salary)


