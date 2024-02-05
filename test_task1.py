import pytest 
import os
import tempfile
from Task1 import countDirectoryAndFiles

@pytest.fixture
def test_create_directory():
    temp_dir=tempfile.mkdtemp()
    return temp_dir



def test_count_directories_and_files_with_one_file_and_one_directory(test_create_directory):
    temp_directory=test_create_directory
    os.makedirs(os.path.join(test_create_directory,'dir1'))
    open(os.path.join(temp_directory,'dir1','file1.txt'),'w').close()
    directoriesAndFiles=countDirectoryAndFiles(temp_directory)
    assert directoriesAndFiles == (1,1)

def test_count_directories_and_files(test_create_directory):
    temp_directory=test_create_directory
    os.makedirs(os.path.join(temp_directory,'dir1'))
    os.makedirs(os.path.join(temp_directory,'dir1','subdir1'))
    open(os.path.join(temp_directory,'dir1','file1.txt'),'w').close()
    open(os.path.join(temp_directory,'dir1','subdir1','sub_file.txt'),'w').close()
    os.chmod(os.path.join(temp_directory,'dir1','subdir1'),0o000)
    directoriesAndFiles=countDirectoryAndFiles(temp_directory)
    assert directoriesAndFiles == (1,2)



def test_read_permission(test_create_directory):
    if not os.access(test_create_directory,os.R_OK):
        with pytest.raises(PermissionError):
            countDirectoryAndFiles(test_create_directory)

def test_write_permission(test_create_directory):
    if not os.access(test_create_directory,os.W_OK):
        with pytest.raises(PermissionError):
            countDirectoryAndFiles(test_create_directory)

def test_execute_permission(test_create_directory):
    if not os.access(test_create_directory,os.X_OK):
        with pytest.raises(PermissionError):
            countDirectoryAndFiles(test_create_directory)

