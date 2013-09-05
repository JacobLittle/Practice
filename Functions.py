"""
Practicing with function use in Python.
"""
def Switch(x, y):
  temp = x
  x = y
  y = temp
  
def DisplayAddition(x, y):
  sum = x + y
  print "\n{} + {} = {}", x, y, sum
  
x = 4
y = 5

Switch(x, y)
print "\n{}, {}", x, y

w = 6
l = 4
DisplayAddition(w, l)
