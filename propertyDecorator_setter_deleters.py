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

    @property #treat the below function as property 
    def email(self):
        if self.fname == None:
            return 'Email not set'
        else:
              return self.fname+'.'+self.lname+'@email.com'
    
    @email.setter
    def email(self,given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]



    @classmethod #decorator
    def change_increment(cls,amount):  #the above decorator declares this as class method for which the argument self is not required
        cls.increment=amount
    @classmethod #decorator
    def from_str(cls,emp_str):
        fname,lname,salary=emp_str.split('-')
        return cls(fname,lname,int(salary))
     
    @email.deleter  #to delete porpety deleter are used
    def email(self):
        self.fname= None
        self.lname= None

    @staticmethod #this means that the file is not concerned with instance or class variable soself or cls keyword are not required
    def isopen(day): #can pass any augument (self or cls not required)
        if day=='Sunday':
            return False
        else:
            return True


if __name__=='__main__':
   harry = Employee('harry','jackson',44000)
   rohan=Employee('rohan','idiot',55000)
   print(harry.email, rohan.email)
   rohan.lname = 'Khanna'
   print(rohan.email)
   rohan.email = 'khanna.rohan@gmail.com'
   print(rohan.email)
   del rohan.email
   print(rohan.email)
