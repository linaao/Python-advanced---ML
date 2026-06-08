# ----------------- introduction -----------------------------------------------------------------------------
stocks = [234, 356, 890, 847, 452, 111]

day_one = stocks[0]
day_three = stocks[2]

print(day_one, day_three)


# ---------  start of the work ----------------------------------------------------------------------------
# ------- finding max of numbers -----------
max_find = [233, 134, 908, 7473, 222, 456, 302, 180, 145]

max_val = max_find[0]
min_val = max_find[0]

for i in range (len(max_find)):
    if max_find[i] > max_val:
        max_val =  max_find[i]
    
    if  max_find[i] < min_val:
        min_val =  max_find[i]
    
print(f"The max value from the array is: {max_val}")
print(f"The min value from the array is: {min_val}")
