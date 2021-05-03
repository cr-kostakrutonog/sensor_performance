import os
import time
# import win32com.client
import win32com.client as win32


def closeXlsxObj():
    excel = win32.Dispatch("Excel.Application")
    excel.Quit()


def createXlsxFile(file_name):
    try:
        excel = win32.Dispatch("Excel.Application")
        workbook = excel.Workbooks.Add()
        workbook.SaveAs(file_name)
        excel.Quit()
        return 1
    except:
        return 0


def openXlsxFile(file_name):
    try:
        # Open Excel and make it visible
        excel = win32.Dispatch('Excel.Application')
        excel.Visible = True
        workbook = excel.Workbooks.Open(file_name)
        excel.Quit()
        return 1
    except:
        return 0


def calculatePersentinle(start_times):
    start_times.sort()
    del start_times[2:len(start_times)]

# def test_set1():
#     home_dir = os.path.expanduser('~')
#     file_path=home_dir + '\\Desktop'
#     file_name='123.xls'
#     closeExcelObj()
#     # createExcelFile('C:\\Users\\kosta.krutonog\\Desktop','123.xls')
#     start = time.time()
#     createExcelFile(file_path,file_name)
#     end = time.time()
#     print(f'Excel creation time:{(end - start):.3f}')
#
#     for _ in range(0, 10):
#         start = time.time()
#         openExcel(file_path,file_name)
#         end = time.time()
#         #print(f'Excel open:{end - start}')
#         start_times.append(end - start)
#
#     removeFile(file_path,file_name)
#
# start_times=[]
# for i in range(0, 10):
#     start_times = []
#     test_set1()
#     print(start_times)
#     np.random.seed(0)
#     #print("Percentile in Test {}:{}.%f1".format(i+1,))
#     print(f'Percentile in Test {i+1}:{np.percentile(start_times, 80):.3f}')
# closeExcelObj()
# excel()
# word()
