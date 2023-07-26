fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


fruits = [2, 10, 20]

for x in fruits:
  y = x /2
  print(int(y))


for  x in "banana":
  print(x)


#looping through a string

for x in "Burhani":
  print(x)



#break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
provinces = ["kabul", "Badakhshan", "Herat", "Nangarhar"]
for x in provinces:
  print(x)
  if x == "Badakhshan":
    break
  

# the continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#The range() Function

for x in range (10):
  print(x)
  
for x in range (10):
  print("Burhani")


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)


#else

for x in range(6):
  print(x)
else:
  print("Finally finished!")



#Break

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement

for x in [0, 1, 2]:
  pass




