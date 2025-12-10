class employee:
    def __init__(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position

    def emp_history(self):
        print(f"employee name is {self.name},his id {self.id} and position is {self.position} ")

emp1=employee("vini",171198,"developer")
emp2=employee("vijay",29909,"tester")

emp1.emp_history()
