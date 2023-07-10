#class employee:
#    company = "google"
#    def getsalary(self):
#        print("salary is 100k")
        
#vijay = employee()
#vijay.getsalary()

#another
class employee:
    company = "google"
    def getsalary(self):
        print(f"the company is {self.company} salary is {self.salary}")
        
vijay = employee()
vijay.salary = 10000
vijay.company

vijay.getsalary()