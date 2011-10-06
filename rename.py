#!python

import EXIF
import sys
import os

list = {}

for filename in sys.argv[1:]:
   try:
       file=open(filename, 'rb')
   except:
       print "'%s': Cannot open for reading.\n" % filename
       continue

   # get the tags
   data = EXIF.process_file(file, details=False, debug=False)
   if not data:
       print '%s: No EXIF data found' % filename
       continue

   date    = data['EXIF DateTimeOriginal']

   key = str(date)
   if key in list.keys():
       print '%s: Duplicate datestamp with %s' % (filename, list[key])
   list[key] = filename

   file.close()

datestamps = list.keys()
datestamps.sort()
for datestamp in datestamps:
   suffix = os.path.splitext(list[datestamp])[1]
   newName = datestamp.replace(':', '_')
   newName = newName.replace(' ', '_')
   newName = "pic" + newName + suffix
   try:
       os.rename(list[datestamp], newName)
       print list[datestamp] + ' -> ' + newName
   except:
       print '%s: Could not rename' % list[datestamp]