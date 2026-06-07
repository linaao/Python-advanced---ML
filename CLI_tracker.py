sessions = []

def menu():
    print("\n ........... Study Tracker ...........")
    print("1. Add new study session")
    print("2. List sessions")
    print("3. Exit")

def session_Add():
    subject = input("Enter your subject: ")
    duration = input("Enter the duration: ")
    date = input ("Enter the date of the study session: ")
    new_sessions = {
        "subject" : subject,
        "duration" : duration,
        "date": date
    }
    sessions.append(new_sessions)
    print("New study session was added successfully!")
    print("Would you like to go back to the menu?")
    menu()
    option  = int(input("Choose a option: "))
    main()



def sessions_show():
    if len(sessions) == 0:
        print("You still have not added any new session today!")
    else:
        for i, session in enumerate(sessions, start=1):
            print("Here is the list of all your saved sessions:  ")
            print(f"Session {i}: {subject} for {duration} minutes, on {date}")


def main():
    menu()

    option  = int(input("Choose a option: "))

    if option == 1:
        session_Add()
    elif option == 2:
        sessions_show()
    elif option == 3:
        print("You are exiting now!")
        

main()
