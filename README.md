![GobBLE's Logo](https://github.com/VirusFriendly/GobBLE/blob/master/assets/GobBLE-logo.png)
# GobBLE

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VirusFriendly/GobBLE/master)

This Jupyter notebook analyzes the RaMBLE database to enumerate new BLE devices and technologies that the analyst may wish to investigate, by reporting device indicators not previously recorded.

# Preview

A static preview can be [found here](https://github.com/VirusFriendly/GobBLE/blob/master/assets/RaMBLE_original.html)

# Get Started

If you're unfamiliar with using Jupyter notebooks, [here's a simple tutorial](http://opentechschool.github.io/python-data-intro/core/notebook.html)

This notebook depends on the database exported by [RaMBLE](https://play.google.com/store/apps/details?id=com.contextis.android.BLEScanner), a passive BLE scanner for Android devices.

Export the RaMBLE database and copy it to the location with the notebook as `RaMBLE.sqlite` and then use the Jupyter notebook as normal.

## Binder Support

[Binder](https://mybinder.org/) allows you to view Jupyter notebooks online. If you would like view this notebook but with your database using Binder, you'll need to have your database accessible online (like Google Drive if you know [this trick](http://thebiobucket.blogspot.com/2011/10/how-to-link-to-google-docs-for-download.html)). Fork this repo, and then change the URL in the [postBuild](https://github.com/VirusFriendly/GobBLE/blob/master/postBuild) file to location of your database. Then submit your repo to [MyBinder.org](https://mybinder.org/).

### CAUTION

The RaMBLE database contains location data, which people can use to track your whereabouts and possibly the location of your home, school, or workplace. If you're concerned about sharing your location data, run the droplocation.py provided in the extras directory.

Example:

With the database in the current directory:

```
python3 droplocation.py
```

or provide the script the location (on your computer) of the database

```
python3 droplocation.py ~/Downloads/RaMBLE.sqlite
```
