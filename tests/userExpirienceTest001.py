import os
import time
import numpy as np
import logging
from pywinauto import application

from sensor_performance.infra import utils
from sensor_performance.infra import notepad
from sensor_performance.infra import compression
from sensor_performance.infra import word
from sensor_performance.infra import excel
from sensor_performance.infra import chrome

# from sensor_performance.infra import chrome
#

iters = 1
results = {}


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            import inspect
            total = 0
            for i in range(iters):
                start = time.time()
                test_status = func(*args, **kwargs)
                # print(f"Test status:{test_status}")
                end = time.time()
                # total = total + (end - start)

                curframe = inspect.currentframe()
                # print(inspect.currentframe())
                calframe = inspect.getouterframes(curframe, 2)
                # print(inspect.getouterframes(curframe, 2))
                test_name = calframe[1][4][1].split('(')[0].replace(" ", "")
                # print('Test name:', test_name)
                # print('[*] Average tests time: {} sec.'.format(total / iters))
                # if test_status == 1:
                results.update({test_name: {'start_time': start, 'end_time': end}})
                # return {test_name: {'start_time': start, 'end_time': end}}
                # elif test_status == 0:
                #     results.update({test_name: {'start_time': 0, 'end_time': 0}})
                # else:
                #     print(test_status)
                #     print("ERROR:Unexpected test status")

        return wrapper

    return actual_decorator


# create txt file 100MB
@benchmark(iters=iters)
def testCreateTxtFile100MB(file_name):
    # size = 1048576  # 1MB
    size = 104857600  # 100MB
    return notepad.createFileBySize(file_name=file_name, file_size=size)


# open txt file 100MB
@benchmark(iters=iters)
def testOpenTxtFile100MB(file_name):
    app = application.Application().start('notepad.exe')
    notepad.openNotepadFile(app, file_name=file_name)
    notepad.closeNotepad(app)


# edit txt file 100MB

# compress txt file 100MB
@benchmark(iters=iters)
def testZippingTxtFile100MB(source_file_name="", compressed_file_name=""):
    # print("Zipping file")
    compression.zipFile(file_for_compression=source_file_name, compressed_file_name=compressed_file_name)


# utils.removeFile(file_name=source_file_name)

# uncompress txt file 100MB
@benchmark(iters=iters)
def testUnzippingTxtFile100MB(compressed_file_name):
    # print("Unzipping file")
    compression.unzipFile(compressed_file_name=compressed_file_name)


# utils.removeFile(file_name=compressed_file_name)
# utils.removeFile(file_name=source_file_name)

# create txt file 500MB
@benchmark(iters=iters)
def testCreateTxtFile500MB(file_name):
    # size = 1048576  # 1MB
    size = 536870912  # 512MB
    return notepad.createFileBySize(file_name=file_name, file_size=size)


# open txt file 500MB
@benchmark(iters=iters)
def testOpenTxtFile500MB(file_name):
    app = application.Application().start('notepad.exe')
    notepad.openNotepadFile(app, file_name=file_name)
    notepad.closeNotepad(app)


# edit txt file 500MB

# compress txt file 500MB
@benchmark(iters=iters)
def testZippingTxtFile500MB(source_file_name, compressed_file_name):
    compression.zipFile(file_for_compression=source_file_name, compressed_file_name=compressed_file_name)


# uncompress txt file 500MB
@benchmark(iters=iters)
def testUnzippingTxtFile500MB(compressed_file_name):
    compression.unzipFile(compressed_file_name=compressed_file_name)


# Open Chrome www.google.com
@benchmark(iters=iters)
def testOpenCromeGoogleSite():
    site_name = 'www.google.com'
    chrome_driver_file_path = home_dir + '\\Downloads\\Selenium\\chromedriver89.exe'
    chrome.openChrome(chrome_driver_file_path, site_name)


# create doc file
@benchmark(iters=iters)
def testCreateDocFile(doc_file_name):
    word.createDocFile(doc_file_name)


# open doc file
@benchmark(iters=iters)
def testOpenDocFile(doc_file_name):
    word.openDocFile(doc_file_name)


# edit doc file
@benchmark(iters=iters)
def testEditDocFile(doc_file_name):
    word.editDocFile(doc_file_name)


# create xlsx file
@benchmark(iters=iters)
def testCreateXlsxFile(xlsx_file_name):
    excel.createXlsxFile(xlsx_file_name)


# open xlsx file
@benchmark(iters=iters)
def testOpenXlsxFile(xlsx_file_name):
    excel.openXlsxFile(xlsx_file_name)


# TODO edit xlsx file

# TODO compress 10 text files
# TODO uncompress 10 text files

# TODO compress 10 files with different extentions
# TODO uncompress 10 files with different extentions

def analysis(test_set_results):
    calculeted_results = []
    tests_names = test_set_results[0].keys()
    print(tests_names)

    tmp_duration = []
    for test_name in tests_names:
        tmp_duration = []
        for tests_set_results in test_set_results:
            for local_test_name, test_results in tests_set_results.items():
                if local_test_name == test_name:
                    tmp_duration.append(test_results.get('end_time') - test_results.get('start_time'))
        # print(test_name,tmp_duration)
        np.random.seed(0)
        calculeted_results.append({test_name: {'min': round(min(tmp_duration), 3), 'max': round(max(tmp_duration), 3),
                                               'avg': round(sum(tmp_duration) / len(tmp_duration), 3),
                                               'percentile': round(np.percentile(tmp_duration, 80), 3)}})
    return calculeted_results


def main():
    logger = logging.getLogger()
    log_format = (
        '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

    # Define basic configuration
    logging.basicConfig(
        # Define logging level
        level=logging.DEBUG,
        # Define the format of log messages
        format=log_format,
        # Provide the filename to store the log messages
        filename=('debug.log'),
    )

    log_file_name = "kk_logging.log"
    delay_between_tests = 1
    test_set_results = []
    home_dir = os.path.expanduser('~')
    file_path = home_dir + '\\Desktop'
    source_file_name = file_path + '\\test1.txt'
    compressed_file_name = source_file_name + '.zip'
    doc_file_name = file_path + '\\test001.docx'
    xlsx_file_name = file_path + '\\test001.xlsx'

    # Test Set running

    for j in range(0, 1):
        test_set_results = []
        curtime = time.localtime(time.time())
        logger.info(
            f"Test set run number {j + 1} start time {curtime.tm_year}-{curtime.tm_mon}-{curtime.tm_mday} {curtime.tm_hour}:{curtime.tm_min}:{curtime.tm_sec}\n")
        for i in range(0, 1):

            if (os.path.exists(source_file_name)):
                utils.removeFile(source_file_name)
            if (os.path.exists(compressed_file_name)):
                utils.removeFile(compressed_file_name)
            if (os.path.exists(doc_file_name)):
                utils.removeFile(doc_file_name)
            if (os.path.exists(xlsx_file_name)):
                utils.removeFile(xlsx_file_name)
            time.sleep(delay_between_tests)

            testCreateTxtFile100MB(source_file_name)
            time.sleep(delay_between_tests)

            testOpenTxtFile100MB(source_file_name)
            time.sleep(delay_between_tests)

            # testZippingTxtFile100MB(source_file_name, compressed_file_name)
            # time.sleep(delay_between_tests)
            #
            # testUnzippingTxtFile100MB(compressed_file_name)
            # time.sleep(delay_between_tests)
            # #
            # if (os.path.exists(source_file_name)):
            #     utils.removeFile(source_file_name)
            # # time.sleep(delay_between_tests)
            #
            # testCreateTxtFile500MB(source_file_name)
            # time.sleep(delay_between_tests)
            #
            # testZippingTxtFile500MB(source_file_name, compressed_file_name)
            # time.sleep(delay_between_tests)
            #
            # testUnzippingTxtFile500MB(compressed_file_name)
            # time.sleep(delay_between_tests)
            #
            # testOpenCromeGoogleSite()
            # time.sleep(delay_between_tests)
            #
            # if (os.path.exists(doc_file_name)):
            #     utils.removeFile(doc_file_name)
            # time.sleep(delay_between_tests)
            #
            # testCreateDocFile(doc_file_name)
            # time.sleep(delay_between_tests)
            #
            # testOpenDocFile(doc_file_name)
            # time.sleep(delay_between_tests)
            #
            # testEditDocFile(doc_file_name)
            # time.sleep(delay_between_tests)
            #
            # utils.removeFile(doc_file_name)
            #
            # if (os.path.exists(xlsx_file_name)):
            #     utils.removeFile(xlsx_file_name)
            # time.sleep(delay_between_tests)
            #
            # testCreateXlsxFile(xlsx_file_name)
            # time.sleep(delay_between_tests)
            #
            # testOpenXlsxFile(xlsx_file_name)
            # time.sleep(delay_between_tests)
            #
            # utils.removeFile(xlsx_file_name)
            #
            test_set_results.append(results)
            logger.info(results)

        curtime = time.localtime(time.time())

        # print(test_set_results)

        calculeted_results = analysis(test_set_results)
        for test_set_result in calculeted_results:
            for test_name, test_result in test_set_result.items():
                logger.info(f"{test_name}, {test_result}")
        logger.info(
            f"Test set run number {j + 1} end time {curtime.tm_year}-{curtime.tm_mon}-{curtime.tm_mday} {curtime.tm_hour}:{curtime.tm_min}:{curtime.tm_sec}\n")

        return results

if __name__ == '__main__':
    main()
