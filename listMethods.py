#append()

fruitslist = ["banana", "mango", "apple", "orange"]
fruitslist.append("kiwi")

print(fruitslist)


#clear()

fruitslist = ["banana", "mango", "apple", "orange"]
fruitslist.clear()

print(fruitslist)

#copy()

fruitslist = ["banana", "mango", "apple", "orange"]

ahmad = fruitslist.copy()
print(ahmad)


#count()

fruitslist = ["banana", "mango", "apple", "orange", "banana", "mango", "apple", "orange"]
x = fruitslist.count("mango")

print(x)

#extent

fruitslist = ['banana', 'mango', 'apple', 'orange']
cars = ['ford', 'BMW', 'Volvo']

fruitslist.extend(cars)

print(fruitslist)

#index()

cars = ['ford', 'BMW', 'Volvo']
x = cars.index("Volvo")

print(x)


#insert()

fruitslist = ['banana', 'mango', 'apple', 'orange']
fruitslist.insert(1, "kiwi")

print(fruitslist)


#pop()

cars = ['ford', 'BMW', 'Volvo']

cars.pop(2)

print(cars)

#remove()

fruitslist = ['banana', 'mango', 'apple', 'orange']
fruitslist.remove("banana")

print(fruitslist)

#reverse()

cars = ['ford', 'BMW', 'Volvo']
cars.reverse()

print(cars)

#sort()

fruitslist = ['banana', 'mango', 'apple', 'orange']

fruitslist.sort()

print(fruitslist)











