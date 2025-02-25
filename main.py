from time import *
























def countdown(hrs: int = 0, mins: int = 0, secs: int = 0) -> None:

    total_seconds = (hrs * 3600) + (mins * 60) + secs

    while total_seconds >= 0:

        print(f"\r{hrs:02d}:{mins:02d}:{secs:02d} left!", end = "")
        total_seconds -= 1
        sleep(1)
        
        hrs = total_seconds // 3600
        remainder = total_seconds - (3600 * hrs)
        mins = remainder // 60
        secs = remainder - (mins * 60)

countdown(1, 1, 0)
