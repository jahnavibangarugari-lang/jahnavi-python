#entire oops program
#inheritance
#method overriding
class employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("employees do the work")
class manager(employee):
    def work(self):
        print(self.name,"the manager manages the team")
class tester(employee):
    def work(self):
        print(self.name,"the teter tests the code")
def employee_details(emp):#common function for all methods
    emp.work()
m=manager("girls")
t=tester("boys")
employee_details(m)
employee_details(t)
