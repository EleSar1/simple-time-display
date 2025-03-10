from time import sleep
from utils import customizable_output


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