from time import *

def display_current_time() -> None:

    process = True
    current_date = strftime("%A, %B %d %Y")

    while process:
        try:
            c_hour = gmtime().tm_hour
            c_minutes = gmtime().tm_min
            c_secs = gmtime().tm_sec

            if c_hour == 0 and c_minutes == 0 and c_secs == 0:
                current_date = strftime("%A, %B %d %Y") #update the current date

            current_time = strftime("%H:%M:%S")
            print(f"{current_date} {current_time}    ", end = "\r")
            if KeyboardInterrupt:
                print("\n")
            sleep(1)
        except KeyboardInterrupt:
            print("\nInterrupted.")
            process = False

display_current_time()