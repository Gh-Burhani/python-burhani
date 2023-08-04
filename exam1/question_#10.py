def print_message(massege, repeat_count):
    for x in range(repeat_count):
        print(massege)

massege = input("Enter message: ")
repeat_count = input("Enter count: ")

print_message(massege, int(repeat_count))
