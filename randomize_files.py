"""
   This script randomizes image files in a directory. The main reason for
   creating this script is to randomize the pics in my desktop wallpaper
   directory. Thus the images show in a different ordered. Note this script
   will fail if there are more than 999 images in the directory.
"""

import os
from random import shuffle
import re

# change this to your directory and run script from command line and make
# sure it ends in a trailing "/".
IMG_DIR = "/home/me/Py_Projects/randomize_files/wallpaper/"
IMG_EXTS = ['jpeg', 'jpg', 'png', 'gif']


def rename_files(old_and_new):
    for files in old_and_new:
        os.rename(files[0], files[1])


def add_zeros(num):
    """This is to preserve ordering in directory later. 001 comes before 010
       before 100. Thus 1st file becomes '001' and 10th file becomes '010'
       and 100 stays at 100."""

    if num < 10:
        return '00' + str(num)
    elif num < 100:
        return '0' + str(num)
    else:
        return str(num)


def preappend(images):
    """Assess if files have been sorted before. If not add numerical prefix
       to files to preserve the randomized order when renamed in directory
       later. If have been previously sorted, replace previously added
       numerical prefix with new numerical prefix."""

    head_tail = [os.path.split(img) for img in images]

    # 3 digits followed by dash is used for numerical ordering
    pattern = r'^\d{1,3}-'
    prefixed = []
    for num, tups in enumerate(head_tail, 1):
        original = os.path.join(tups[0], tups[1])
        prefix = add_zeros(num) + '-'
        if re.match(pattern, tups[1]) is None:
            prefixed.append((original, os.path.join(tups[0],
                             prefix + tups[1])))
        else:
            prefixed.append((original, os.path.join(tups[0],
                             re.sub(pattern, prefix, tups[1]))))

    rename_files(prefixed)


def randomize_files(images):
    """Randomize order of the files in list"""
    shuffle(images)
    preappend(images)


def get_images(file):
    """Only return files with image extensions"""

    for ext in IMG_EXTS:
        if file.lower().endswith(ext):
            return True


def get_files():
    """Get list of files in directory (os.listdir()) excluding directories
       and non image files"""

    randomize_files([x for x in (filter(get_images,
                     (IMG_DIR + x for x in os.listdir(IMG_DIR)
                      if os.path.isfile(IMG_DIR + x))))])


def main():
    get_files()


if __name__ == '__main__':
    main()
