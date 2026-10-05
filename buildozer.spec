
[app]

# (str) Title of your application
title = Calendar App

# (str) Package name
package.name = calendarapp

# (str) Package domain (needed for android packaging)
package.domain = org.calendar.app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (list) Android architecture to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
