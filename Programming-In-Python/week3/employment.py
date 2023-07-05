class Employee():
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password


class Chef(Employee):
    def leave_request(self, days):
        return "May I take a leave forf " + str(days) + "days?"


andrian = Employee("Adrian", "A")
emily = Supervisor("Emily", "Herny", "1234")
niko = Chef("Niko", "Gomez")
print(niko.leave_request(5))
