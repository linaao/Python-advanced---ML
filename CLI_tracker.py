sessions = []

while True:
    print("\n ........... Study Tracker ...........")
    print("1. Add new study session")
    print("2. List sessions")
    print("3. Exit")

    option  = int(input("Choose a option: "))

    if option == 1:
        subject = input("Enter your subject: ")
        duration = input("Enter the duration: ")
        date = input ("Enter the date of the study session: ")
        new_sessions = [subject, duration, date]
        sessions.append(new_sessions)
        print("New study session was added successfully!")

    elif option == 2:
        print("Here is the list of all your saved sessions:  ")
        for i, session in enumerate(sessions, start=1):
            print(f"Session {i}: {session[0]} for {session[1]} minutes, on ")



