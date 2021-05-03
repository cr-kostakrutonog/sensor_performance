import os
import random
import string
import time
import zipfile

from urllib3.connectionpool import xrange
# file_name="C:\\Users\\kosta.krutonog\\Desktop\\bla.txt"
# t0 = time.time()
# open("bla.txt", "wb").write("q")
# d = time.time() - t0
# print("duration: %.2f s." % d)


def zipFile(file_for_compression="",compressed_file_name=""):
    try:
        my_zipfile = zipfile.ZipFile(compressed_file_name, mode='w', compression=zipfile.ZIP_DEFLATED)
        my_zipfile.write(file_for_compression)
        my_zipfile.close()
        return 1
    except:
        return 0

def unzipFile(compressed_file_name):
    try:
        my_zipfile = zipfile.ZipFile(compressed_file_name)
        my_zipfile.extractall()
        return 1
    except:
        return 0




