from datetime import *

currentDate = datetime.now().date()
schedule = [ datetime.combine(currentDate, time(8, 0)),
	           datetime.combine(currentDate, time(8, 55)),
	           datetime.combine(currentDate, time(9, 50)),
	           datetime.combine(currentDate, time(10, 45)),
	           datetime.combine(currentDate, time(11, 40)),
	           datetime.combine(currentDate, time(12, 35)),
	           datetime.combine(currentDate, time(13, 30)),
	           datetime.combine(currentDate, time(14, 25)),
	           datetime.combine(currentDate, time(15, 20)),
	           datetime.combine(currentDate, time(16, 20)) ]

periods = ["1st", "2nd", "3rd", "4th", "5th",  "6th", "7th", "8th", "9th", "10th"]

def current_period():
  current = datetime.now()
  for i in range(len(schedule)):
      if schedule[i] > current:
          return i
  return 0

def return_difference():
  current = current_period()
  if current == 9:
      current = 0

  difference = schedule[current] - datetime.now()
  difference = (':'.join(str(difference).split(':')[:2])).split(" ")[::-1]
  return difference[0] + " untill " + str(periods[current])
