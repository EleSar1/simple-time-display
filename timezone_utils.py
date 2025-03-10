from datetime import datetime 
from pytz import timezone, all_timezones
from time import sleep


def timezone_converter(location: str) -> None:

    """
    Continuously displays the current time in the specified timezone.

    This function retrieves the current time for the given timezone and updates 
    it every second in an infinite loop. The user can stop the process manually 
    by pressing `Ctrl + C`, which will trigger a `KeyboardInterrupt` and exit 
    the loop gracefully.

    Args:
        -location (str): The name of the timezone (e.g., "Europe/Rome", "America/New_York").

    Returns:
    None
    """

    tz = timezone(location)
    process = True
    while process:
        try:
            time_tz = datetime.now(tz=tz).strftime("%B %d %Y %H:%M:%S %Z %z")
            print(f"\r{time_tz}", end="")
            sleep(1)
        except KeyboardInterrupt:
            print("\nProgram interrupted by the user. Goodbye!")
            process = False


def world_clock_display(tz_choice = list) -> None:
    
    """
    Displays the current time for a list of specified timezones.

    This function takes a list of timezone names and prints the current time 
    in each of them. The time is formatted as "Month Day Year HH:MM:SS". 

    Args:
        tz_choice (list): A list of strings representing timezone names 
                          (e.g., ["Europe/Rome", "America/New_York"]).

    Returns:
        None
    """    """
    Displays the current time for a list of specified timezones.

    This function takes a list of timezone names and prints the current time 
    in each of them. The time is formatted as "Month Day Year HH:MM:SS". 

    Args:
        tz_choice (list): A list of strings representing timezone names 
                          (e.g., ["Europe/Rome", "America/New_York"]).

    Returns:
        None
    """
    
    for location in tz_choice:
        tz = timezone(location)
        time_tz = datetime.now(tz=tz).strftime("%B %d %Y %H:%M:%S")
        print(f"Time in {location}: {time_tz}")