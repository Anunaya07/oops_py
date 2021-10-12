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

    def __add__(self,other): #this is a dunder method you cannot add to classes but this is add the as defined
        return self.salary + other.salary
    def __repr__(self):#print uses repr dunder so to change what is printed dunder can be use:d
        return 'Employee({},{},{})'.format(self.fname,self.lname,self.salary)
    def __str__(self):
        return 'Name of the Employee is  {}.'.format(self.fname)



harry = Employee('harry','jackson',44000)
rohan=Employee('rohan','idiot',55000)
print(repr(harry))
#print(harry) is run the __str__() method
