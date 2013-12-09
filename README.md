RaspiStill_Camera_Options
==============
A python script that tests multiple exposure and auto white balance settings using RaspiStill and the Raspberry Pi camera module.

Installation
------------
```
$ wget https://github.com/ntalekt/RaspiStill_Camera_Options/blob/master/raspistill_camera_options.py
```

Rationale
---------
When taking timelapse or general pictures with the Raspberry Pi camera module using RaspiStill you wonder what the best settings would be for a particular photo setting.

This script will take pictures using the different exposure and auto white balance settings to let you easily find the best settings for your photo session. You can quickly run this script and look through the picture output to decide what the best settings are for a particular photo setting. 

Configuration
---------
You can choose between three different lists each outputs a different amount of test pictures.

* Full list: Outputs 120 test pictures using all available options
* Refined list: Outputs 50 pictures using the most used options
* Test list: Outputs 3 pictures using auto settings

Remove the comments from the "list_ex" and "list_awb" of the list you want to use (only use one list at a time). For instance I have commented out the 'Test list' in the example below:
```
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
```

Usage
-----
```
$ python raspistill_camera_options.py

```

Original Project
-----
* Original project URL: [Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/?p=1862)
