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

    @staticmethod #this means that the file is not concerned with instance or class variable soself or cls keyword are not required
    def isopen(day): #can pass any augument (self or cls not required)
        if day=='Sunday':
            return False
        else:
            return True
harry = Employee('harry','jackson',44000)
'''lovish = Employee.from_str("lovish-jackson-23000")
rohan = Employee('rohan','das',74000)'''
print("Using class name:")
print("Monday:",Employee.isopen('Monday'))

print("using instance name:")
print("SUnday:",harry.isopen("Sunday"))
