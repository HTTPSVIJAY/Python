class Employee:
    company = 'bahrat gas'
    salary = 500
    salarybounus = 400
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybounus
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybounus = val - self.salary
    
e = Employee()
print(e.totalsalary)
e.totalsalary = 5800
print(e.salary)
print(e.salarybounus)