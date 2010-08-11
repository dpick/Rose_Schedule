from datetime import *

schedule = [
time(8, 0),
time(8, 55),
time(9, 50),
time(10, 45),
time(11, 40),
time(12, 35),
time(13, 30),
time(14, 25),
time(15, 20),
time(16, 20)
]

for i in range(len(schedule)):
    schedule[i] = datetime.combine(datetime.now().date(), schedule[i])

periods = ["1st", "2nd", "3rd", "4th", "5th",  "6th", "7th", "8th", "9th", "10th"]

def current_period():
    current = datetime.now()
    for i in range(len(schedule)):
        if schedule[i] > current:
            return i
    return 0

current = current_period()
if current == 9:
    current = 0


difference = schedule[current] - datetime.now()
difference = (':'.join(str(difference).split(':')[:2])).split(" ")[::-1]
print difference[0] + " untill " + str(periods[current])