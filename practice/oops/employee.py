class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
name=input()
salary=int(input())
department=input()
obj=Employee(name,salary,department)
obj.display()