#!/usr/bin/python
# raspistill_camera_options.py
# Takes a sequence of photos with the Pi camera
# using a range of Exposure and White Balance
# settings.
#
# Original project URL : http://www.raspberrypi-spy.co.uk/?p=1862
#
# Version 1.0
# Original Author : Matt Hawkins
# Original Date   : 21/06/2013
#
# Version 1.1
# Author : Rick Rocklin
# Date : 07/12/2013
# Modified options to match with most recent RaspiStill binary version, added automatic folder creation
# Date : 11/12/2013
# Added fgallery integration to automatically scrape image output and create a preview gallery for easy viewing.
# Added list menu, and choice to create gallery
import os
import time
import subprocess
import distutils.core
import SimpleHTTPServer
import SocketServer
import socket
from datetime import datetime

## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Full list (120 photos)")
print ("2. Refined list (50 photos)")
print ("3. Test list (3 photos)")
print (30 * '-')
 
## Get input ###
choice = raw_input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
choice = int(choice)
yes = set(['yes','y','ye','Y'])
no = set(['no','n','N'])
gallerychoice = raw_input('Would you like to create a preview gallery? [y/n] : ') 

### Take action as per selected menu-option ###
if choice == 1:
        print ("Starting capture using full list...")
elif choice == 2:
        print ("Starting capture using refined list...")
elif choice == 3:
        print ("Starting capture using test list...")
else:    ## default ##
        print ("Invalid number. Try again...")

if choice == 1:
# Full list of Exposure and White Balance options. 120 photos
	list_ex  = ['auto','night','nightpreview','backlight',
            'spotlight','sports','snow','beach','verylong',
            'fixedfps','antishake','fireworks']
	list_awb = ['off','auto','sun','cloud','shade','tungsten',
            'fluorescent','incandescent','flash','horizon']

elif choice == 2:
# Refined list of Exposure and White Balance options. 50 photos.
	list_ex  = ['auto','night','backlight','spotlight','fireworks']
	list_awb = ['off','auto','sun','cloud','shade','tungsten','fluorescent','incandescent','flash','horizon']

else:
# Test list of Exposure and White Balance options. 3 photos.
	list_ex  = ['auto']
	list_awb = ['off','auto','sun']

# EV level
photo_ev = 0

# Photo dimensions and rotation
photo_width  = 800
photo_height = 600
photo_rotate = 0

photo_interval = 0.25 # Interval between photos (seconds)
photo_counter  = 0    # Photo counter

total_photos = len(list_ex) * len(list_awb)

# Delete all previous image files
try:
  os.remove("photo_*.jpg")
except OSError:
  pass

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# Define the location where you wish to save files. Set to HOME as default.
folderToSave = "raspistill_options_" + str(initYear) + str(initMonth) + str(initDate) + str(initHour) + str(initMins)
os.mkdir(folderToSave)
# Lets start taking photos!
try:

#  print "Starting photo sequence"

  for ex in list_ex:
    for awb in list_awb:
      photo_counter = photo_counter + 1
      filename = 'photo_' + ex + '_' + awb + '.jpg'
      cmd = 'raspistill -o ' + str(folderToSave) + "/" + filename + ' -t 1000 -ex ' + ex + ' -awb ' + awb + ' -ev ' + str(photo_ev) + ' -w ' + str(photo_width) + ' -h ' + str(photo_height) + ' -rot ' + str(photo_rotate)
      pid = subprocess.call(cmd, shell=True)
      print ' [' + str(photo_counter) + ' of ' + str(total_photos) + '] ' + filename    
      time.sleep(photo_interval)

  print "Finished photo sequence"
  if gallerychoice in yes:
   print "Starting gallery creation"
   subprocess.call(['./fgallery', folderToSave, folderToSave])  
   viewDirectory = "./view"
   distutils.dir_util.copy_tree(viewDirectory, folderToSave)
   print "Photos located here: ./" +folderToSave
   os.chdir(folderToSave)
   PORT = 8000
   Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
   httpd = SocketServer.TCPServer(("", PORT), Handler)
   print "Point your browser to http://<yourIPaddress>:",PORT
   httpd.serve_forever()
  else:
   print "Photos located here: ./" +folderToSave     
  

except KeyboardInterrupt:
  # User quit
  print "\nGoodbye!"
