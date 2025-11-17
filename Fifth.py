class Employee:
    salary = 50000
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
         self.increment = ((salary/self.salary)-1)*100

e = Employee()
#print(e.salaryAfterIncrement)  # Output: 60000.0
e.salaryAfterIncrement = 72000
print(e.increment)  # Output: 72000.0