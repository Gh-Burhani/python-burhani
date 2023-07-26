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