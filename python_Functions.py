#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

def my_Speech():
    print("Hello from a function")

my_Speech()



def math(number1):
    print(number1 * 20)
    print(number1 + 100)


math(3)
math(54)


def math(number1):
    print(number1 * 365)
    print(number1 * 365 * 60)

math(24)


def calculateHourAndMinute(data):
    # Hour
    print(data * 365)

    #minute
    print(data * 365 * 60)

calculateHourAndMinute(24)


math(24)




def greet_user(name):
    print("Hello", name)
greet_user("Burhani")


def calculate_rectangle_area(width, height):
    print(width * height)

calculate_rectangle_area(5, 8)


#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#Example
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def car_nam(*cars):
    print("the reed car is " + cars[3])

car_nam("Camry", "Cadillas", "Cooper", "Enzo")



#Keyword Arguments
#You can also send arguments with the key = value syntax.

#his way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(country, province, city):
  print(country)
  print(province)
  print(city)

my_function(country = "Afghanistan", province = "Kabul", city = "taimani")


def my_function(country, province, city, code):
  print("i am from" + country + " My province and cit is " + province + city +str(code))
 

my_function(country = "Afghanistan", province = "Kabul", city = "taimani", code =" +93")



#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#Example
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




#Default Parameter Value
#The following example shows how to use a default parameter value.

#If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(country = "Afghanistan"):
  print("I am from " + country)

my_function("turkia")
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_freinds(name = "Muhamad"):
   print("my best freind is " + name)

my_freinds(" Younus")
my_freinds()
my_freinds("najib")




#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

#E.g. if you send a List as an argument, it will still be a List when it reaches the function:


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values
#To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass


#Recursion
"""Python also accepts function recursion, 
which means a defined function can call itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit
 of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as 
it can be quite easy to slip into writing a function which 
never terminates, or one that uses excess amounts of memory or 
processor power. However, when written correctly recursion can 
be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we
 have defined to call itself ("recurse"). We use the k 
 variable as the data, which decrements (-1) every time 
 we recurse. The recursion ends when the condition is 
 not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how 
exactly this works, best way to find out is by testing and modifying it."""

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# # Home Work

# def print_message(message, repeat_count = 1):
#    x = 1
#    while x<=repeat_count:
#       print(message)
#       x +=1

# print_message("Hello Afghanistan", 10)









