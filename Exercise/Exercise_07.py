from abc import ABC, abstractmethod
 
class Employee(ABC):
 
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
 
    @abstractmethod
    def calculate_base_salary(self):
        pass
 
    def get_info(self):
        return f"Employee: {self.name}, Experience: {self.experience} years, Salary: ${self.salary}"
 
 
class Developer(Employee):
    programming_languages = []
 
    def __init__(self, name, experience, programming_languages):
        super().__init__(name, experience)
        self.programming_languages = programming_languages
 
    def calculate_base_salary(self):
        self.salary = self.experience * 12000 + 2000
 
    def get_info(self):
        return super().get_info() + ", Languages Known - " + str(self.programming_languages)
 
 
class Manager(Employee):
    team_size = 0
 
    def __init__(self, name, experience, team_size):
        super().__init__(name, experience)
        self.team_size = team_size
 
    def calculate_base_salary(self):
        self.salary = self.experience * 12000 + 5000
 
 
developer = Developer("Akshay Developer", 5, ["Python", "Java"])
manager = Manager("Sudhir Manager", 8, 5)
 
developer.calculate_base_salary()
print(developer.get_info())
manager.calculate_base_salary()
print(manager.get_info())