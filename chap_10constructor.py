class Employee:
    company = "google"
    
    def __init__(self,name,salary,subnet):
        self.name = name
        self.salary = salary
        self.subnet = subnet
        print("constructor is created..!")
        
    def getdetails(self):
        print(f"the name is {self.name}")
        print(f"the salary is {self.salary}")
        print(f"the subnet is {self.subnet}")
            
    def getsalary(self):
        print(f"the company is {self.company} salary is {self.salary}")
sagar = Employee("vijay", 100,"youtube")
sagar.getdetails()
sagar.getsalary()