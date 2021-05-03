import os
import time

# import win32com.client
import win32com.client as win32

RANGE = range(3, 8)


def createDocFile(file_name):
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Add()
        word.Visible = True
        rng = doc.Range(0, 0)
        rng.InsertAfter('Hacking Word with Python\r\n\r\n')
        word.ActiveDocument.SaveAs(file_name)
        doc.Close(False)
        word.Application.Quit()
        return 1
    except:
        return 0


def openDocFile(file_name):
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(file_name)
        word.Visible = True
        doc.Close(False)
        word.Application.Quit()
        return 1
    except:
        return 0


def editDocFile(file_name):
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(file_name)
        word.Visible = True
        # time.sleep(5)
        rng = doc.Range(0, 0)
        rng.InsertAfter('Hacking Word with Python\r\n\r\n')
        for i in RANGE:
            rng.InsertAfter('Line %d\r\n' % i)
        rng.InsertAfter("\r\nPython rules!\r\n")
        word.Visible = True
        word.ActiveDocument.SaveAs(file_name)
        doc.Close(False)
        word.Application.Quit()
        return 1
    except:
        return 0


def calculatePersentinle(start_times):
    start_times.sort()
    del start_times[2:len(start_times)]

# def word_test_set1():
#     for _ in range(0, 10):
#         start = time.time()
#         createWord(file_path,file_name)
#         end = time.time()
#         #print(f'Word creation time:{(end - start):.3f}')
#         start_times.append(end - start)
#         removeFile(file_path,file_name)

# start_times=[]
# for i in range(0, 10):
#     start_times = []
#     word_test_set1()
#     print(start_times)
#     np.random.seed(0)
#     start_times.sort()
#     print(start_times)
#     print(f'Percentile in Test {i+1}:{np.percentile(start_times, 80):.3f}')
