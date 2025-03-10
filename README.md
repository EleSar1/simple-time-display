# Simple Time Display Program

## Description

This Python program provides various time management functionalities, including:

- Real-time display of the current time
- Countdown timer
- Stopwatch with pause and resume functionality
- Time zone conversion
- Simultaneous display of multiple time zones

## Features

1. **Current Time Display**

   - Can be stopped with `Ctrl+C`.
   - Shows the current date and time, updating every second.
   - Optionally provides additional information about the week and day of the year.

2. **Countdown Timer**

   - Allows setting a countdown by specifying hours, minutes, and seconds.
   - Supports different display formats:
     - `dhms`: Days, hours, minutes, and seconds.
     - `hms`: Hours, minutes, and seconds.
     - `ms`: Minutes and seconds.
     - `s`: Seconds only.

3. **Stopwatch**

   - Starts a stopwatch to track elapsed time.
   - Can be stopped with `Ctrl+C` and provides options to:
     - Resume timing.
     - Reset the stopwatch.
     - Terminate the program.

4. **Time Zone Conversion**

   - Displays the current time for a specified time zone, updating every second.
   - Can be stopped with `Ctrl+C`.

5. **Multiple Time Zone Display**

   - Allows viewing up to 5 time zones simultaneously.

## Installation

Ensure you have Python 3 installed on your system. Additionally, install the `pytz` module if it is not already present:

```sh
pip install pytz
```

## Usage

Run the program with:

```sh
python time_display.py
```

Follow the on-screen instructions to select the desired functionality.


## Dependencies

- `time`
- `datetime`
- `pytz`


