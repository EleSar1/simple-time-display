from time import localtime, strftime, sleep 


def display_current_time() -> None:
    
    """
    Continously displays the current date and time in the format:
    Day, Month DD YYYY HH:MM:SS TZ %z", updating every second.

    The function runs indefinitely until interrupted by the user (with Ctrl+C).
    When interrupted, it prints "Interrupted by the user." and terminates gracefully.

    The displayed date is updated at midnight to ensure accuracy.

    Dependencies: 
    - Uses 'strftime' and 'localtime' from the 'time' module.
    - Uses 'sleep' from the 'time' module to update every second.

    Example output:

        ''' 
        March 04 2025 14:30:45 CET +0100
        '''

    Args: 

        None
    
    Returns:

        None
    """

    process = True
    current_date = strftime("%B %d %Y")

    while process:
        try:
            local_time = localtime()
            c_hour = local_time.tm_hour
            c_minutes = local_time.tm_min
            c_secs = local_time.tm_sec

            if c_hour == 0 and c_minutes == 0 and c_secs == 0:
                current_date = strftime("%B %d %Y") #update the current date

            current_time = strftime("%H:%M:%S %Z %z")
            print(f"\r{current_date} {current_time}   ", end = "")
            sleep(1)
        except KeyboardInterrupt:
            print("\nInterrupted by the user.\n")
            process = False


def display_date_information() -> str:
    """
    Returns a string containing information about the current date.

    The returned string includes:
    - The full name of the current day (e.g., Monday, Tuesday).
    - The week number of the year (starting from 00).
    - The day number of the year (starting from 001).

    Returns:
        str: A formatted string with the current date information.
    """
        
    date_information = strftime("It's %A, is the %U week number and  %j day of the year.")
    return date_information