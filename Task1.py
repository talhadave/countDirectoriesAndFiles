import os
def countDirectoryAndFiles(path):

    print("adding some debud satement")
    files =directories = 0

    for _, dirnames, filenames in os.walk(path):
         files += len(filenames)
         directories += len(dirnames)


    return (files,directories)
    
    print("adding another debugging statement")
    

path=os.getcwd()
print(countDirectoryAndFiles(path))
