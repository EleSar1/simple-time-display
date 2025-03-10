from display import display_current_time, display_date_information
from timezone_utils import timezone_converter, world_clock_display
from time_operations import countdown, stopwatch
from pytz import all_timezones


def main():

    print("Welcome to Simple Time Display program.\nPlease choose an option by pressing:\n")
    print("1: to display current time.")
    print("2: to start a countdown.")
    print("3: to start stopwatch.")
    print("4: to start the timezone converter.")
    print("5: to start multiple clock display.")
    print("Press 0 if you want to stop the program.")
    print("\n-------------------------------------------------------------------------------\n")

    choice = -1
    while choice > 5 or choice < 0: 
        try: 
            choice = int(input("Insert choice here: "))
            if choice > 5:
                print("\nNumber out of range. Please make sure to choose an existing functionality.")
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")

    if choice == 1:
        print("\nDisplay current time\n")
        display_current_time()

        additional_information = ""
        while additional_information != "Y" and additional_information != "N":
            additional_information = input("Do you want to display additional information (e.g, the day of the week)? (Y/N)").upper()
            if additional_information != "Y" and additional_information != "N":
                print("Please enter a valid answer (Y/N).")
            elif additional_information == "Y":
                print(display_date_information())


    elif choice == 2:
        print("\nStarting Countdown\n")
        
        hrs = -1

        while hrs < 0: 
            try:
                hrs = int(input("Please enter the hours as integer: "))
                if hrs < 0:
                    print("\nInvalid input. Please make sure to enter a positive number.")
            except ValueError:
                print("\nInvalid input. Please enter an integer.")

        mins = -1

        while mins < 0: 
            try:
                mins = int(input("Please enter the minutes as integer: "))
                if mins < 0:
                    print("\nInvalid input. Please make sure to enter a positive number.")
            except ValueError:
                print("\nInvalid input. Please enter an integer.")

        secs = -1 

        while secs < 0:
            try:
                secs = int(input("Please enter the seconds as integer: "))
                if secs < 0:
                    print("\nInvalid input. Please make sure to enter a positive number.")
            except ValueError:
                print("\nInvalid input. Please enter an integer.")

        format_countdown = ["dhms", "hms", "ms", "s", "0"]
        display_format = ""
        while display_format not in format_countdown:
            display_format = input("Please specify which format you want to use (dhms/hms/ms/s)\n0 to exit.\n")
            if display_format not in format_countdown:
                print("Wrong input. Please make sure to insert an existing format.")
            elif display_format in format_countdown[0:4]:
                countdown(hrs, mins, secs, display_format)
                print("\nTime's up!")
            elif display_format == "0":
                print("Terminated by the user. Goodbye!")

    elif choice == 3:
        print("\nStarting Stopwatch.\nPress Ctrl+C to stop.")
        stopwatch()
        print("Exiting. . .\nGoodbye!")

    elif choice == 4:
        print("\nStarting the time zone converter.\nPress Ctrl+C when you want to stop.\n")

        location = ""
        while location not in all_timezones and location != "0":    
            location = input("Please enter the timezone you want to be displayed (e.g, Australia/Melbourne)(0 to exit): ")
            if location not in all_timezones and location != "0":
                print("This location does not exist. Make sure to enter an existing timezone.\n")
            elif location == "0":
                print("Program interrupted by the user. Goodbye!!")
            else:
                print(f"\nDate and time in {location}:")
                timezone_converter(location)

    elif choice == 5:
        
        print("Starting multiple clocks display.\nThis program allows you to display up to 5 different clock simoultaneously.\n")

        timezones = []
        
        for counter in range(1,5+1):
            location_choice = input(f"Location number {counter}: ")
            while location_choice not in all_timezones:
                location_choice = input("Please enter a valid location (e.g, 'America/New_York', 'Europe/Rome'): ")
            timezones.append(location_choice)
        world_clock_display(timezones)

       
if __name__ == "__main__":
    
    main()