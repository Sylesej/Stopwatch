#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""This script is an advanced stopwatch
designed for use by the DTU Roadrunners
at the Shell Eco Marathon. v0.1 by Nils
Toudal."""

#Import needed functions
import time
import sys
import linecache
import os

################################################################################

def start():
    goOn = False
    #This function defines the start time if the user chooses to.
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
            goOn = False
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
  elif place == 't':
    return 't'
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

def comment(times,zonedict,sectors,type):
    #expected- and actual time as function of type
    lap = sectors.count(1)
    if type=='s':
        expected = zonedict[sectors[-1]][1]
        actual = times[-1]
        typel = 'sector'
    elif type=='l':
        expected = 0
        for n in range(sectors[-1]):
            expected = expected + zonedict[n+1][1]
        actual = 0
        for n in range(sectors[-1]):
            actual = actual + times[-n-1]
        typel='lap'
    elif type=='r':
        expected = 0
        for item in zonedict.values():
            expected = expected + item [1]
        expected = expected * (sectors.count(1)-1)
        for n in range(sectors[-1]):
            expected = expected + zonedict[n+1][1]
        actual = sum(times)
        typel='race'

    if actual<expected:
        text = ' seconds faster than expected in this '
        return str(expected-actual) + text + typel
    else:
        text = ' seconds slower than expected in this '
        return str(actual-expected) + text + typel

def analyze(data,zonedict,metadict):
    #Read file from beginning, file is read on every itteration of while loop.
    #Not super elegant.
    data.seek(4,0)
    #Read data into content, to treat as a str
    content = data.read()
    #Split data into each line, will output a 2d array
    splits = content.splitlines()
    times = [0]*len(splits)
    sector = [0]*len(splits)
    for n in range(len(splits)):
        #Convert to string to use string methods. Back to 1d array.
        splits[n] = str(splits[n])
        #Split by space, into 2d again
        splits[n] = splits[n].split()
        #Time is first, then sector indicator.
        times[n] = float(splits[n][0])
        sector[n] = int(splits[n][1])

    seccom = comment(times,zonedict,sector,'s')
    lapcom = comment(times,zonedict,sector,'l')
    raccom = comment(times,zonedict,sector,'r')

    print 'Sector: ' + str(sector[n]) + ' Time: ' + str(times[n]-times[n-1])
    print 'This sector you are: '+ seccom
    print 'On this lap you are: ' + lapcom
    print 'In this race you are: '+ raccom
    #print 'Time remaining: ' + str(metadict['Timelimit']-times[-1])


def trackdict(trackfile):
    track.seek(0,0)
    #Read data into content, to treat as a str
    tcontent = track.read()
    tcontent = str(tcontent)
    tcontent = tcontent.split('zones:\n')
    tmeta = tcontent[0]
    tmeta = tmeta.split()
    metadict = {'Trackname': tmeta[1], 'Mapfile': tmeta[3],
    'Timelimit': float(tmeta[5]), 'Tracklength': float(tmeta[7]),
    'Laps': int(tmeta[9])}
    tcontent = tcontent[1]
    tcontent = tcontent.split()
    zonedict = {}
    for n in range(len(tcontent)/2):
        zonedict[n+1] = [int(tcontent[n*2]),int(tcontent[n*2+1])]
    return [metadict,zonedict]


################################################################################


#Ask user for output file name and trackname
#For development 'trackdata.txt' and 'some.dat ' are selected
filename = 'some.dat' #raw_input('Select a name for your output data file: ')
trackfile = 'trackdata.txt' #raw_input('Enter name of track data file: ')
mapfile = linecache.getline('trackdata.txt',4)
mapfile = mapfile[0:len(mapfile)-1]

#Files are opened
data = open(filename,'w+')
track = open(trackfile,'r')
themap = open(mapfile,'r')

data.write('0 0\n')

#Before printing anything, clear terminal
os.system('clear')

#Map is printed from file and file is closed again.
trackname = linecache.getline('trackdata.txt',2)
print '\n \nThis is a map of ' + trackname
print themap.read()
themap.close()

#Zones area loaded from trackfile
zonedict = trackdict(trackfile)[1]
metadict = trackdict(trackfile)[0]

#Zones are printed
for item in zonedict:
    p1 = 'Zone: ' + str(item)
    p2 = ' Zonelength: ' + str(zonedict[item][0])
    p3 = ' Expected time: ' + str(zonedict[item][1]) + '\n'
    print p1 + p2 + p3

#Time is started by user command
tStart = start()

#Race is going on as long as the user wants
race = 'go'
entries = 1
os.system('clear')
while race != False:
    themap = open(mapfile,'r')
    #themap.seek(0.0)
    print themap.read()
    themap.close()
    #Analyze data on every run exept the first
    if race == True:
        analyze(data,zonedict,metadict)
    elif race == 't':
        print 'Time now: ' + str(time.time()-tStart)
        print 'Time remaining '+str(metadict['Timelimit']-time.time()+tStart)
    race = lapTime(tStart)
    #Clear terminal
    os.system('clear')

print 'Results of this run:\n'
data.seek(4,0)
print data.read()

################################################################################

#At end files are closed for safety
track.close()
data.close()
