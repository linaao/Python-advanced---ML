from calculator import square

def main():
    test_sqea()

def test_sqea():
    try:
        assert square(2) == 4
        assert square(3) == 9

    except AssertionError:
        print("IT's true mate..........")
if __name__ == "__main__":
    main()