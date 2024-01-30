import os
def countDirectoryAndFiles(path):

    files =directories = 0

    for _, dirnames, filenames in os.walk(path):
        files += len(filenames)
        directories += len(dirnames)

    print (f"Number of files are :{files} and number of directories are {directories}")

path=os.getcwd()
countDirectoryAndFiles(path)
