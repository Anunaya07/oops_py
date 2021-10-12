class Employee: #class defining
    increment = 1.5
    no_of_employee=0
    def __init__(self,fname,lname,salary): #defining constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employee+=1
    def increase1(self):
        self.salary=int( self.salary * self.increment) #first searches instance variables then searches class variables
        '''
        1) This increment directly won't take 1.5 as given
        2) First it will search the above instance varaiable  and then it will search in the class variable.
        3)so to make it search only in class variable we have to mention class name before it 

        for example in the above given example:
        --> self.increment should be replaced by Employee.increment
        '''
    def increase2(self):
        self.salary=int(self.salary * Employee.increment) #searches only class variables

print("Initial number of Employee:",Employee.no_of_employee)
harry=Employee("harry","bhai",44000)
print("all class variables:\n",Employee.__dict__)
print("all instance variable:\n",harry.__dict__)
print("----")
print("using class variable:")
print(harry.salary)
harry.increase2()
print(harry.salary)
print("---")
print("Using instance variable:")
harry.increment=1.2
print("updated instance variable:",harry.__dict__)
harry.salary=44000
print(harry.salary)
harry.increase1()
print(harry.salary)
print("----")
print("No of employee:")
print("employee count in the middle:",Employee.no_of_employee)
rohan=Employee("rohan","silver",56000)
print("final number of Employee:",Employee.no_of_employee)

