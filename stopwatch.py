"""This script is an advanced stopwatch
designed for use by the DTU Roadrunners
at the Shell Eco Marathon. v0.1 by Nils
Toudal."""

#Import needed functions
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
  #This function writes the time since startTime in datafile choosen by user
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

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def load_track(track):
    len = file_len(trackfile)
    zones = [0]*len
    for n in range(len):
        zones[n] = linecache.getline('trackdata.txt',13+n)
    return zones





#Ask user for output file name and trackname
#For development 'trackdata.txt' can be used.
filename = raw_input('Select a name for your output data file: ')
trackfile = raw_input('Enter name of track data file: ')
mapfile = linecache.getline('trackdata.txt',4)
mapfile = mapfile[0:len(mapfile)-1]

#Files are opened
data = open(filename,'w')
track = open(trackfile,'a')
themap = open(mapfile)

#Map is printed from file and file is closed again.
print 'This is a map of your track: '
print themap.read()
themap.close()

zones = load_track(track)
track.close()
for obj in zones:
    print obj

#Time is started by user command
tStart = start()

#Race is going on as long as the user wants
race = True
while race != False:
  race = lapTime(tStart)


#At end files are closed for safety
data.close()
