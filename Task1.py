import os
def countDirectoryAndFiles(path):
     
     print("hello")
     files =directories = 0

     for _, dirnames, filenames in os.walk(path):
         files += len(filenames)
         directories += len(dirnames)

     print("world")

     return (files,directories)
     
    

path=os.getcwd()
print(countDirectoryAndFiles(path))
