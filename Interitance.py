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

class Programmer(Employee): #inherits all the methods in Employee class
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary)
        self.proglang=proglang
        self.exp=exp
    def increase(self): #overwrite the method inherited from employee class
        self.salary=int( self.salary * (self.increment+0.2))

harry = Programmer('harry','jackson',44000,'python','5 yrs')
help(Programmer) #help() shows how the programmers class is resolved
