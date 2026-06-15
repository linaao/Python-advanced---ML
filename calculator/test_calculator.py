from calculator import square

def main():
    test_sqea()

def test_sqea():
    if square(2) != 4:
        print("Squared of 2 was not 4! repeat ")
    if square(3) != 3:
        print("Squared of 3 was not 9! repeat ")

if __name__ == "__main__":
    main()