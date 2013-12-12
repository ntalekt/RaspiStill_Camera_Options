RaspiStill_Camera_Options 
============== 
A python script that tests multiple exposure and auto white balance settings using RaspiStill and the Raspberry Pi camera module. 
The script will optionally create a local gallery for easy viewing of the photos.

Installation
------------

Download the package:
```
$ wget **PLACEHOLDER FOR tar.gz**
```
Extract the package:
```
$ tar -xzvf PLACEHOLDER FOR tar.gz**
```

Dependencies
---------
Frontend/gallery: none (static html/js/css)

Backend:

* ImageMagick (http://www.imagemagick.org)
* Either:

  - ``exiftran`` (part of ``fbida``: http://www.kraxel.org/blog/linux/fbida/), or
  - ``exifautotran`` (part of ``libjpeg-progs``: http://libjpeg.sourceforge.net/).

* zip
* perl, with the following additional modules:

  - JSON::PP (libjson-perl and optionally libjson-xs-perl)
  - Date::Parse (libtimedate-perl)

The following is optional, but used when installed:

* jpegoptim (http://www.kokkonen.net/tjko/projects.html)
* pngcrush (http://pmt.sourceforge.net/pngcrush/)
* facedetect (http://www.thregr.org/~wavexx/hacks/facedetect/)

Install all the required dependencies with:
```
sudo apt-get install imagemagick exiftran zip libjson-perl libtimedate-perl
```

Rationale
---------
When taking timelapse or general pictures with the Raspberry Pi camera module using RaspiStill you wonder what the best settings would be for a particular photo setting.

This script will take pictures using the different exposure and auto white balance settings to let you easily find the best settings for your photo session. You can quickly run this script and look through the picture output to decide what the best settings are for a particular photo setting. 

Usage
-----
```
$ python raspistill_camera_options.py
```

You can use the menu to choose between three different lists each outputs a different amount of test pictures.

* Full list: Outputs 120 test pictures using all available options
* Refined list: Outputs 50 pictures using the most used options
* Test list: Outputs 3 pictures using auto settings

  ```
  ------------------------------
     M A I N - M E N U
  ------------------------------
  1. Full list (120 photos)
  2. Refined list (50 photos)
  3. Test list (3 photos)
  ------------------------------
  Enter your choice [1-3] :
  ``` 

The script will also optionally create a local preview gallery and host the website for easy preview:
```
Would you like to create a preview gallery? [y/n] :
```

```
Point your browser to http://192.168.1.100:8000
```

Screenshot of the preview gallery:
![Gallery preview screenshot](http://ntalekt.com/images/SS_Raspi_fgallery.png)

Project credits
-----
* Original code source: [Raspberry Pi Spy](http://www.raspberrypi-spy.co.uk/?p=1862)
* Heavily modified by me.
