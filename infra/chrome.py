from selenium import webdriver


def openChrome(chrome_driver_file_path,site_name):
    try:
        https_protocol="https://"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(options=options, executable_path=chrome_driver_file_path)
        #driver.get('https://docs.google.com/spreadsheets/d/1ZJ7D1cHPN03hCkuFd6YfecPAX9sxjxMgFXh2Rh68LXo')
        driver.get(https_protocol+site_name)
        driver.title
        driver.close()
        return 1
    except:
        return 0

# home_dir = os.path.expanduser('~')
# site_name='www.facebook.com'
# chrome_driver_file_path = home_dir + '\\Downloads\\Selenium\\chromedriver89.exe'
# openChrome(chrome_driver_file_path,site_name)