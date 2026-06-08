try:
    nm = int(input("what's x? "))
    print(f"X is: {nm}")
except ValueError:
    print("X is not an integer")