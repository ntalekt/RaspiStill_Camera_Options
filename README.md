Script to test different exposure and auto white balance settings using RaspiStill and the Raspberry Pi camera module. This lets you easily find the best settings for your photo setting.

Script will create a directory and name the picture accordingly so you can easily isolate which picture settings were used in the capture.

Defaults: 
photo_width  = 1920
photo_height = 1080
photo_rotate = 0

Remove the comments from the "list_ex" and "list_awb" of the list you want (i.e. Full list - 120 pictures, Refined list - 50 pictures, Test list - 3 pictures).

Run using: 
python raspistill_camera_options.py
