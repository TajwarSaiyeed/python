import datetime
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_date():
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, date_str.split('-'))
            return datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Please try again.")


def get_event():
    return input("Enter event: ")


def view_events(events):
    for event in events:
        print(event)


def main():
    events = {}
    while True:
        clear()
        print("1. Add event")
        print("2. View events")
        print("3. Exit")
        choice = input("Enter choice: ")
        clear()
        if choice == '1':
            date = get_date()
            event = get_event()
            if date in events:
                events[date].append(event)
            else:
                events[date] = [event]
        elif choice == '2':
            view_events(events)
            input("Press enter to continue.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press enter to continue.")


if __name__ == '__main__':
    main()
