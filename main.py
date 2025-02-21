from time import *

def display_current_time() -> None:

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
            print("\nInterrupted.")
            process = False

display_current_time()