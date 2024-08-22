import time
import sys
from src.segment import Segment
from src.display import Display

display = Display(dimension=(1000, 40))


def get_time() -> dict[str, str]:
    """
    Gets the current time and returns a stringified version of the hour and minute.
    """
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    seconds = current_time.tm_sec
    return {"hour": str(hour), "minute": str(minute), "seconds": str(seconds)}


def display_clock(show_seconds_line: bool = False):
    time_data = get_time()
    # Pad hour and minute with leading zeros if necessary
    time_data["hour"] = time_data["hour"].zfill(2)
    time_data["minute"] = time_data["minute"].zfill(2)

    # Set digits on the display
    display.set_digit(time_data["hour"][0], 0)
    display.set_digit(time_data["hour"][1], 9)
    display.set_digit(time_data["minute"][0], 27)
    display.set_digit(time_data["minute"][1], 36)

    display.set_digit("1", 18) if show_seconds_line else display.delete_digit(18)

    sys.stdout.write("\033[H")  # ANSI escape code to move the cursor to the top left
    print(display, end="")

if __name__ == "__main__":
    l = True
    try:
        # This clears the screen initially and hides the cursor
        sys.stdout.write("\033[2J\033[?25l")
        while True:
            display_clock(show_seconds_line=l)
            l = not l
            time.sleep(1)
    except KeyboardInterrupt:
        # Reset cursor visibility on exit
        sys.stdout.write("\033[?25h\nEnd!\n")
        sys.exit(0)
