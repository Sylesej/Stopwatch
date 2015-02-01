"""This script is an advanced stopwatch
designed for use by the DTU Roadrunners
at the Shell Eco Marathon. v0.1 by Nils
Toudal."""

import time
import sys
import linecache

def start():
  #This function defines the start time if the user chooses to.
  goOn = False

  while goOn!=True:
    inp = raw_input('Enter S for Start or E for Exit: ')
    if inp == 'S':
      tStart = time.time()
      goOn = True
    elif inp == 'E':
      print 'You terminated the program.'
      print 'Goodbye'
      sys.exit()
    else:
      print 'Your input was not accepted.'
      print 'Please enter a valid input.'

    return tStart

def lapTime(startTime): #, data
  #This function writes the time since startTime in data
  place = raw_input('Enter a position on the track: ')
  if place == 'E':
    print 'You terminated the program.'
    print 'Goodbye'
    return False
  else:
    t = time.time()
    delta = t - startTime
    data.write(str(delta) + '    ' + place + '\n')
    print ' '*20 + 'Time: ' + str(delta) + ' '*4 + 'Position: '+ place
    return True


filename = raw_input('Select a name for your output data file: ')
trackfile = raw_input('Enter name of track data file: ')
mapfile = linecache.getline('trackdata.txt',4)
mapfile = mapfile[0:len(mapfile)-1]

data = open(filename,'w')
track = open(trackfile,'a')
themap = open(mapfile)

print 'This is a map of your track: '
print themap.read()
themap.close()

tStart = start()

race = True
while race == True:
  race = lapTime(tStart)

data.close()
track.close()
