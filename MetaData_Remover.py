import os, sys
from PIL import Image
from six.moves import input
image_file = input("[ > ] Enter the path of image : ")
if os.path.isfile(image_file):
    directory, filename = os.path.split(image_file)
    image = Image.open(image_file)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(directory + "/Deleted_Metadata" + filename )
    print("[ > ] New File Saved : %s/Deleted_Metadata%s" % (directory,filename))
    sys.exit(0)
else:
    print("[ > ] Image Path Does not Exists !")