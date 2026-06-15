
# name = input("What's your name??")
# with open("names.txt" , 'a') as file:
# file.write(f"{name}\n")

names = []
with open("names.txt" , 'r') as file:
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
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"HEllo to {name}")