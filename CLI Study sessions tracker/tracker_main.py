import json

def load_sessions():
    #Tries to load data from the JSON file. If it doesn't exist, returns an empty list
        try:
            with open('sessions.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []


def save_sessions():
    # Saves the current sessions list into the JSON file
        with open('sessions.json' ,'w') as file:
            json.dump(sessions,file)



sessions = load_sessions()

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


def sessions_show():
    if len(sessions) == 0:
        print("You still have not added any new session today!")
    else:
        print("Here is the list of all your saved sessions:  ")
        for i, session in enumerate(sessions, start=1):
            print(f"Session {i}: {session['subject']} for {session['duration']} minutes, on {session['date']}")


def main():
    while True:
        menu()
        option  = int(input("Choose a option: "))

        if option == 1:
            session_Add()
        elif option == 2:
            sessions_show()
        elif option == 3:
            print("You are exiting now!")
            break
        else:
            print("You entered an invalid option, please choose again: ")
           

main()
