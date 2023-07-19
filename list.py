pythonStudents = ["Ahamad", "Zafar", "Jaihoon", "Safa", "Zafar", "Jaihoon", "Safa"]
print(pythonStudents)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(len(pythonStudents))


newStudents = ["Karim", "Ali", "Rahim", "Jamil", "Rashid", "Belal", "Rahmat"]

print(newStudents)
print(len(newStudents))
print(newStudents[3])
print(newStudents[-1]) # if we us - the search wii start form the end of the list.
print(newStudents[2:4])
print(newStudents[:3])
print(newStudents[1:])
print(newStudents[-3:-1])

if "Akram" in newStudents:
    print("present")
else:
    print("absent")

if "Ali" in newStudents:
    print("present")

newStudents = ["Karim", "Ali", "Rahim", "Jamil", "Rashid", "Belal", "Rahmat"]
pythonStudentsold = ["Karim", "Ali", "Rahim", "Jamil", "Rashid"]

newStudents[3] = "Akram"
print(newStudents)

#add

newStudents.append("Qamar")
print(newStudents)

newStudents.extend(pythonStudentsold)
