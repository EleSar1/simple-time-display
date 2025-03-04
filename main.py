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
