import os
def countDirectoryAndFiles(path):
    
    print("add debug statement")
    files =directories = 0

    for _, dirnames, filenames in os.walk(path):
         files += len(filenames)
         directories += len(dirnames)


    return (files,directories)
     
    

path=os.getcwd()
print(countDirectoryAndFiles(path))
