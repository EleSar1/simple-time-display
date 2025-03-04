from time import *
























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

