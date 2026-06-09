# we can write it like this:

#while True:
#        try:
 #           nm = int(input("what's x? "))
 #           break
 #       except ValueError:
 #           print("X is not an integer")
# or like this: 
def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass

main()

   