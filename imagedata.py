from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn): # opens image "fn" (filename) and extracts and decodes the metadata by converting the tags to a more intelligible form
    ret = {}
    pic = Image.open(fn)
    info = pic._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag)
        ret[decoded] = value
    return ret

# change the parameter to get_exif to refer to a file on your own machine
# it is simplest to put the image in the same folder as your code
tags = get_exif("/Users/lindam/Pictures/ethanwallace.JPG")

#print (type(tags))
#print (tags)
print ("gps: ", type(tags["GPSInfo"]))

#for key,value in tags.items():
#   print (key,value)

for tag in tags:
    print (tag)
print (tags["GPSInfo"])