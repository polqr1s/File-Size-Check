import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

path = askdirectory(title='Select Folder')
os.chdir(path)
flist = open('todelete.txt')


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
    

def deletefiles():
    print('Are you sure you want to delete these files and their directories?')
    deletecheck = input('type \'delete\' to start deleting')
    if deletecheck == 'delete':
        flist.seek(0)#Lets the file be re-read
        for f in flist:
            fname = f.rstrip()
            for dirpath, dirnames, filenames in os.walk(fname):
                for indFiles in filenames:
                    fullPath = os.path.join(dirpath, indFiles)
                    if os.path.isfile(fullPath):
                        os.remove(fullPath)
                        print ('Deleted', fullPath)
                    if os.path.isdir(dirpath):
                        if len(os.listdir(dirpath)) == 0:
                            print(dirpath, 'is empty')
                            os.rmdir(dirpath)
                            print ('Deleted', dirpath)
    else:
        print('Deletion aborted')


filesize()
deletefiles()
flist.close()





