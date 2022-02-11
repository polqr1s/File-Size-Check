import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

path = askdirectory(title='Select Folder')
os.chdir(path)
flist = open('test.txt')

def filesize():
    total_size = 0
    for f in flist:
        fname = f.rstrip()
        for dirpath, dirnames, filenames in os.walk(fname):
            for indFiles in filenames:
                fullPath = os.path.join(dirpath, indFiles)
                size = os.path.getsize(fullPath)
                print (size, 'bytes', indFiles)
                if not os.path.islink(fullPath):
                    total_size += size
    print (total_size, 'bytes total')

filesize()
flist.close()





