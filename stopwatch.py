"""This script is an advanced stopwatch
designed for use by the DTU Roadrunners
at the Shell Eco Marathon. v0.1 by Nils
Toudal."""

#Import needed functions
import time
import sys
import linecache
import os

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
      print 'Goodbye\n'
      sys.exit()
    else:
      print 'Your input was not accepted.'
      print 'Please enter a valid input.'

    return tStart

def lapTime(startTime): #, data
  #This function writes the time since startTime in datafile choosen by user
  leng = str(file_len(trackfile) - 12)
  print  'There are ' + leng + ' positions on the track.'
  text = 'Enter a position between 1 and ' + leng +', or enter E for exit: '
  place = raw_input(text)
  if place == 'E':
    print 'You terminated the program.'
    print 'Goodbye \n'
    return False
  else:
    t = time.time()
    delta = t - startTime
    data.write(str(delta) + ' ' + place + '\n')
    #print ' '*22 + 'Time: '+ str(delta) + ' '*4 + 'Position: ' + place + '\n'
    return True

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def load_track(track):
    leng = file_len(trackfile) - 12
    zones = [0]*leng
    for n in range(leng):
        zones[n] = linecache.getline('trackdata.txt',13+n)
        zones[n] = zones[n][0:len(zones[n])-1]
        zones[n] = str(zones[n])
        zones[n] = zones[n].split(' ',2)
    return zones

def analyze(zones,data,trackfile):
    print 'I analyze stuff.'



#Ask user for output file name and trackname
#For development 'trackdata.txt' and 'some.dat ' are selected
filename = 'some.dat' #raw_input('Select a name for your output data file: ')
trackfile = 'trackdata.txt' #raw_input('Enter name of track data file: ')
mapfile = linecache.getline('trackdata.txt',4)
mapfile = mapfile[0:len(mapfile)-1]

#Files are opened
data = open(filename,'w')
track = open(trackfile,'a')
themap = open(mapfile,'r')

#Before printing anything, clear terminal
os.system('clear')

#Map is printed from file and file is closed again.
trackname = linecache.getline('trackdata.txt',2)
print '\n \nThis is a map of ' + trackname
print themap.read()
themap.close()

#Zones are printed
zones = load_track(track)
a = 1
for obj in zones:
    print 'Zone ' + str(a) + ' length: ' + obj[0] + ', expected time: ' + obj[1]
    a = a + 1
print '\n'

#Time is started by user command
tStart = start()

#Race is going on as long as the user wants
race = 'go'
os.system('clear')
while race != False:
    themap = open(mapfile,'r')
    print themap.read()
    themap.close()
    #Analyze data on every run exept the first
    if race == True:
        analyze(zones,data,trackfile)
    race = lapTime(tStart)
    #Clear terminal
    os.system('clear')

data.close()

result = open(filename,'r')
print result.read()

#At end files are closed for safety
result.close()
track.close()
