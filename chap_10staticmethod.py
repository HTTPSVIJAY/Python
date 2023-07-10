class employee:
    company = "google"
    def getsalary(self):
        print(f"the company is {self.company} salary is {self.salary}")
        
    @staticmethod  
    def greet():
        print('good morning sir..!')
        
sagar = employee()
sagar.salary = 10000
#sagar.company
sagar.greet()
sagar.getsalary()