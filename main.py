from time import *


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
            print(f"{current_date} {current_time}   ", end = "\r")
            sleep(1)
        except KeyboardInterrupt:
            print("\nInterrupted by the user.")
            process = False
            
          
def countdown(hrs: int = 0, mins: int = 0, secs: int = 0) -> None:

    """

    Runs a countdown timer from the specified hours, minutes, and seconds.

    The countdown updates every second and display the remaining time in the format: "HH:MM:SS left!". 
    The function runs until the timer reaches 00:00:00

    Args:
        - hrs (int): The number of hours to count down from (default is 0).
        - mins (int): The number of minutes to count down from (default is 0).
        - secs (int): The number of seconds to count down from (default is 0).

    Returns:
        None

    Behavior:
        - The function continuously updates the displayed time using a carriage return ('\n') to
          overwrite the previous output.
        - The countdown ends automatically when it reaches zero.

    Example usage:

    '''
        countdown(0,1,10) # Starts a countdown from 1 minute and 10 seconds
    '''    
    
    """

    total_seconds = (hrs * 3600) + (mins * 60) + secs

    while total_seconds >= 0:

        print(f"\r{hrs:02d}:{mins:02d}:{secs:02d} left!", end = "")
        total_seconds -= 1
        sleep(1)
        
        hrs = total_seconds // 3600
        remainder = total_seconds - (3600 * hrs)
        mins = remainder // 60
        secs = remainder - (mins * 60)


def stopwatch() -> None:

    total_secs = 0
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
            print("\nInterrupt detected. Exiting . . .")
            process = False


def main():

    print("Welcome to Simple Time Display program.\nPlease choose an option:")
    print("Press [1] to display current time.")
    print("Press [2] to start a countdown.")
    print("Press [3] to start stopwatch.")

    