import os


def removeFile(file_name):
    try:
        os.remove(file_name)
        return 1
    except:
        print(f"ERROR:unable to remove file {file_name}")
        return 0