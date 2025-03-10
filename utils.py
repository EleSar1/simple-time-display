def customizable_output(total_seconds: int, display_format: str) -> str:
    
    """
    Formats the given total time in seconds into a human-readable string 
    based on the specified display format.

    Parameters:
    total_seconds (int): The total duration in seconds.
    display_format (str): The desired output format. Options:
        - "dhms": Days, hours, minutes, and seconds (e.g., "1 days, 02:30:15")
        - "hms": Total hours, minutes, and seconds (e.g., "26:30:15")
        - "ms": Total minutes and seconds (e.g., "1590:15")
        - "s": Only seconds (e.g., "95415 seconds")

    Returns:
    str: The formatted time string according to the chosen display format.
    """

    days = total_seconds // 86400
    hrs = (total_seconds % 86400) // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    if display_format == "dhms":
        return f"{days} days, {hrs:02d}:{mins:02d}:{secs:02d}"
    elif display_format == "hms":
        total_hours = total_seconds // 3600
        return f"{total_hours:02d}:{mins:02d}:{secs:02d}"
    elif display_format == "ms":
        total_minutes = total_seconds // 60
        return f"{total_minutes:02d}:{secs:02d}"
    elif display_format == "s":
        return f"{secs:02d} seconds"