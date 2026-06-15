def creat():
    name = input("What's your name??")
    with open("names.txt" , 'a') as file:
        file.write(f"{name}\n")
    

creat()

with open("names.txt" , 'r') as file:
     lines = file.readlines()

for line in lines:
    print("HEll000 to, ", line)
    