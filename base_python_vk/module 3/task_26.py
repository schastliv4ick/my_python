class Person:
   def __init__(self, _age):
       self._age = _age

   @property
   def age(self):
       return self.age

   @age.setter
   def age(self, value):
        if value < 0:
           self.age = 0
        else:
           self.age = value
           

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)