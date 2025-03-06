from time import localtime, strftime, sleep
from datetime import datetime
from pytz import all_timezones, timezone

def display_current_time() -> None:
    
    """
    Continously displays the current date and time in the format:
    Day, Month DD YYYY HH:MM:SS", updating every second.

    The function runs indefinitely until interrupted by the user (with Ctrl+C).
    When interrupted, it prints "Interrupted by the user." and terminates gracefully.

    The displayed date is updated at midnight to ensure accuracy.

    Dependencies: 
    - Uses 'strftime' and 'localtime' from the 'time' module.
    - Uses 'sleep' from the 'time' module to update every second.

    Example output:

        ''' 
        Monday, March 04 2025 14:30:45
        '''

    Args: 

        None
    
    Returns:

        None
    """

    process = True
    current_date = strftime("%A, %B %d %Y")

    while process:
        try:
            local_time = localtime()
            c_hour = local_time.tm_hour
            c_minutes = local_time.tm_min
            c_secs = local_time.tm_sec

            if c_hour == 0 and c_minutes == 0 and c_secs == 0:
                current_date = strftime("%A, %B %d %Y") #update the current date

            current_time = strftime("%H:%M:%S")
            print(f"\r{current_date} {current_time}   ", end = "")
            sleep(1)
        except KeyboardInterrupt:
            print("\nInterrupted by the user.")
            process = False

            
def customizable_output(total_seconds: int, display_format: str) -> str:
    
    """
    Formats the given total time in seconds into a human-readable string 
    based on the specified display format.

    Parameters:
    total_seconds (int): The total duration in seconds.
    display_format (str): The desired output format. Options:
        - "dhms": Days, hours, minutes, and seconds (e.g., "1 days, 02:30:15")
        - "hms": Total hours, minutes, and seconds (e.g., "26:30:15")
        - "ms": Total minutes and seconds (e.g., "1590:15")
        - "s": Only seconds (e.g., "95415 seconds")

    Returns:
    str: The formatted time string according to the chosen display format.
    """

    days = total_seconds // 86400
    hrs = (total_seconds % 86400) // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    if display_format == "dhms":
        return f"{days} days, {hrs:02d}:{mins:02d}:{secs:02d}"
    elif display_format == "hms":
        total_hours = total_seconds // 3600
        return f"{total_hours:02d}:{mins:02d}:{secs:02d}"
    elif display_format == "ms":
        total_minutes = total_seconds // 60
        return f"{total_minutes:02d}:{secs:02d}"
    elif display_format == "s":
        return f"{secs:02d} seconds"


def timezone_converter(location: str) -> None:
    
    if location in all_timezones:

        tz = timezone(location)
        time_tz = datetime.now(tz=tz)
        print(time_tz)


def countdown(hrs: int = 0, mins: int = 0, secs: int = 0, display_format="hms") -> None:

    """

    Runs a countdown timer from the specified hours, minutes, and seconds.

    The countdown updates every second and display the remaining time in the format: "HH:MM:SS left!". 
    The function runs until the timer reaches 00:00:00

    Args:
        - hrs (int): The number of hours to count down from (default is 0).
        - mins (int): The number of minutes to count down from (default is 0).
        - secs (int): The number of seconds to count down from (default is 0).
        - display_format (str): The format time will be displayed the countdown (default is 'hms').
            Available formats:
            -"dhms" -> Days, hours, minutes, and seconds (e.g., "1 days, 02:30:15")
            - "hms" -> Total hours, minutes, and seconds (e.g., "26:30:15")
            - "ms" -> Total minutes and seconds (e.g., "1590:15")
            - "s" -> Only seconds (e.g., "95415 seconds")

    Returns:
        None

    Behavior:
        - Updates the displayed time every second using a carriage return ('\r') to overwrite previous output.
        - The countdown ends automatically when it reaches zero.
        - Uses the 'customizable_output' function to format the remaining time.

    Example usage:

    '''
        countdown(0,1,10, "hms") # Starts a countdown from 1 minute and 10 seconds
    '''    
    
    """

    total_seconds = (hrs * 3600) + (mins * 60) + secs

    while total_seconds >= 0:

        print(f"\r{customizable_output(total_seconds, display_format)} left!", end = "")
        total_seconds -= 1
        sleep(1)


def stopwatch(total_secs: int = 0) -> None:

    """
    Runs a simple stopwatch using the format 'HH:MM:SS'.

    Args:
        total_secs (int): the total seconds elapsed during stopwatch. Default value is set to 0.
    
    Returns: 
        None

    Behavior:
        - The function continuously updates the displayed time using a carriage return ('\r') to
          overwrite the previous output.
        - The function stop when user prompts 'Ctrl + C'
        - When prompted Ctrl+C, the user can prompt an integer to terminate the program, 
          reset stopwatch to start from 0 again or continue the previous execution.

    """

    process = True

    while process == True:
        
        try:
            hrs = total_secs // 3600
            remainder = total_secs % 3600
            mins = remainder // 60 
            secs = remainder % 60

            print(f"\r{hrs:02d}:{mins:02d}:{secs:02d}", end="")
            total_secs += 1
            sleep(1)

        except KeyboardInterrupt:
            print("\n\nInterrupted. Please type:")
            print("\n1: if you want to resume.")
            print("2: if you want to reset.")
            print("0: if you want to stop.")

            choice = -1
            while choice < 0 or choice > 2:
                try:
                    choice = int(input(""))
                    if choice < 0 or choice > 2:
                        print("Number out of range. Please enter a number between 0 and 2.")
                except ValueError:
                    print("Wrong value. Please enter a valid integer.")
            
            if choice == 1:
                print("Resuming. . .\nPress Ctrl+C to stop")
                stopwatch(total_secs)
            elif choice == 2:
                print("Restarting. . .\nPress Ctrl+C to stop")
                stopwatch()
            

            process = False
 

def main():

    print("Welcome to Simple Time Display program.\nPlease choose an option by pressing:\n")
    print("1: to display current time.")
    print("2: to start a countdown.")
    print("3: to start stopwatch.")
    print("Press 0 if you want to stop the program.")
    print("\n-------------------------------------------------------------------------------\n")

    choice = 4
    while choice > 3 or choice < 0: 
        try: 
            choice = int(input("Insert choice here: "))
            if choice > 3:
                print("\nNumber out of range. Please make sure to choose an existing functionality.")
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")

    if choice == 1:
        print("\nDisplay current time\n")
        display_current_time()

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


if __name__ == "__main__":
    
    main()