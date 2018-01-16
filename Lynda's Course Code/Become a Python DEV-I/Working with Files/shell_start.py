import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists('newfile.txt'):
        # get the path to the file in the current directory
        src = path.realpath('newfile.txt')

        # full path with file name at the end
        print(src)

        # separate the path part from the filename
        head, tail = path.split(src)
        print(head)
        print(tail)

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # now use the shell to make a copy of the file
        shutil.copy(src, dst)

        # copy over the permissions, modification times, and other info
        shutil.copystat(src, dst)

        # renames existing file
        os.rename('textfile.txt', 'newfile.txt')

        # adds the all files to zip file
        root_dir, tail = path.split(src)
        shutil.make_archive('archive', "zip", root_dir)

        # creates a zip file only selected
        with ZipFile('testzip.zip', 'w') as newzip:
            newzip.write('newfile.txt')
            newzip.write('textfile.txt.bak')
main()

