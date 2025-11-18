class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Name:",self.name)
        print("ID:",self.id)
class Employee(Person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,id)
a=Employee("John","12345","1250000","SVP")
a.display()
                            