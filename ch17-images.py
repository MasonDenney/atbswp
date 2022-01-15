"""
### MANIPULATING IMAGES
"""
"""
#
"""
"""
#
"""
"""
### Project: Adding a Logo
#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue    # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    # Save changes.
    im.save(os.path.join('withLogo', filename))

"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
#
"""
"""
### Practice Project: Identifying Photo Folders on Hard Drive
#! python3
# Import modules and write comments to describe this program.
for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if TODO:
            numNonPhotoFiles += 1
            continue    # skip to next filename
        # Open image file using Pillow.
        # Check if width & height are larger than 500.
        if TODO:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
    # If more than half of files were photos,
    # print the absolute path of the folder.
    if TODO:
        print(TODO)
"""
"""
#
"""