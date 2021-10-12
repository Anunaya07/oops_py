class Employee: #class defining
    increment = 1.5
    no_of_employee=0
    def __init__(self,fname,lname,salary): #defining constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employee+=1
    def increase(self):
        self.salary=int( self.salary * self.increment)
    @classmethod #decorator
    def change_increment(cls,amount):  #the above decorator declares this as class method for which the argument self is not required
        cls.increment=amount
    @classmethod #decorator
    def from_str(cls,emp_str):
        fname,lname,salary=emp_str.split('-')
        return cls(fname,lname,int(salary))
harry = Employee('harry','jackson',44000)
lovish = Employee.from_str("lovish-jackson-23000")
rohan = Employee('rohan','das',74000)
print(type(lovish.salary))
