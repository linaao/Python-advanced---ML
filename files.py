
# name = input("What's your name??")
# with open("names.txt" , 'a') as file:
# file.write(f"{name}\n")

# names = []
# with open("names.txt" , 'r') as file:
    #  lines = file.readlines()

# 1st method to remove the ectra new lines after reading the txt file ! -----
# -------------------------------------------------------------------------
# for line in lines:
#     print("HEll000 to, ", line.rstrip())
    
# 2nd method to do it , we removed the the 8th line before this
#--------------------------------------------------------------------------
    # for line in file:
    #     print("HElloo to,", line.rstrip())

# ----------------------------------------
# to sort them out using names = [] now:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"HEllo to {name}")

# 3rd method to write the code is as follows, while removing the list names 
# names = []
# with open ("names.txt", 'r') as file:
#     for line in sorted(file, reverse=True):
#         names.append(line.strip())
#     print(names)

# for name in names[2:4]:
#     print(f"Hello to, {name}")



# with open("students.csv", 'r') as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         print(f"{name} is in {house}")

students = []

with open("students.csv", 'r') as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name,
                   "house" : house}
        students.append(student)
        

for student in sorted(students , key=lambda student: student["name"] ):
    print(f"{student ['name']} is in {student ['house']}  ")