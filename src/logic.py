
#from _typeshed import ProfileFunction
import time
import sys
from segment import Segment
from display import Display


def get_time_str():
    """
    Gets the current time and returns a stringified version of the hour and minute.
    """
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    return f"{hour:02}:{minute:02}"
  
if __name__ == "__main__":
    display = Display(dimension=(6, 7))
    display.add_digit("9")
    
    print(str(display))