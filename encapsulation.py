class Person:
    def __init__(self, name, age):
        self._name=name
        self._age=age
        
    def get_name(self):
        return self._name
        
    def set_name(self,name):
        self._name=name
        
    def get_age(self):
        return self._age
        
    def set_age(self,age):
        self._age=age
        
suman = Person('suman kumar', 20)
suman.set_name('rohan')
# print(suman.get_name())
# print(suman.age) #error

# p=Person('a', 20)
# print(p.name)