class Circle:
   pi = 3.14

   def calculate_area(self, radius):
       s = self.pi * radius ** 2
       return s

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)