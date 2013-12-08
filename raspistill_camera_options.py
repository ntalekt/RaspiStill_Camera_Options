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
#
import os
import time
import subprocess
from datetime import datetime
# Full list of Exposure and White Balance options. 120 photos
#list_ex  = ['auto','night','nightpreview','backlight',
#            'spotlight','sports','snow','beach','verylong',
#            'fixedfps','antishake','fireworks']
#list_awb = ['off','auto','sun','cloud','shade','tungsten',
#            'fluorescent','incandescent','flash','horizon']

# Refined list of Exposure and White Balance options. 50 photos.
#list_ex  = ['auto','night','backlight','spotlight','fireworks']
#list_awb = ['off','auto','sun','cloud','shade','tungsten','fluorescent','incandescent','flash','horizon']

# Test list of Exposure and White Balance options. 3 photos.
list_ex  = ['auto']
list_awb = ['off','auto','sun']

# EV level
photo_ev = 0

# Photo dimensions and rotation
photo_width  = 1920
photo_height = 1080
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

  print "Starting photo sequence"

  for ex in list_ex:
    for awb in list_awb:
      photo_counter = photo_counter + 1
      filename = 'photo_' + ex + '_' + awb + '.jpg'
      cmd = 'raspistill -o ' + str(folderToSave) + "/" + filename + ' -t 1000 -ex ' + ex + ' -awb ' + awb + ' -ev ' + str(photo_ev) + ' -w ' + str(photo_width) + ' -h ' + str(photo_height) + ' -rot ' + str(photo_rotate)
      pid = subprocess.call(cmd, shell=True)
      print ' [' + str(photo_counter) + ' of ' + str(total_photos) + '] ' + filename    
      time.sleep(photo_interval)
  
  print "Finished photo sequence"
  
except KeyboardInterrupt:
  # User quit
  print "\nGoodbye!"
