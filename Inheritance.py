class Car:
    def __init__(self, model, horn):
        self.model=model
        self.horn=horn
    
    def start_car(self):
        return f"car started"
    
    def horn_car(self):
        return f"{self.horn} sound"

class Ford(Car):
    def detail(self):
        return f"{self.horn} {self.model}"
    
c = Ford('h100', 'horse')
print(c.detail())
print(c.horn_car())
print(c.start_car())