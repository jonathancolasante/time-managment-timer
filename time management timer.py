import time
import os

#Setting to modify for personal preference
cycles = 3
work_time = 45 #minutes
break_time = 5 #minutes

#Do not touch these settings
count = 0
phase = "nbreak"


def notification(title, message):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(message, title))


while count <= cycles:
    if phase == "nbreak":
        if count != 0:
            notification("Time Is Up", "Get back to work!")
        else:
            notification("Time started", "Get to work!")
        phase = "break"
        count += 1
        time.sleep(work_time*60)
    else:
        notification("Time Is Up", "Take a " + str(break_time) + " minute break!")
        phase = "nbreak"
        time.sleep(break_time*60)
        count += 1
