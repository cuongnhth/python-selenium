from selenium import webdriver
def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir="+filePath)
    driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe', options=chrome_options)
    return driver
def ham_surf_face(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.facebook.com')
filePath = 'Nick_a'
#Nick_a se dk luu tru trong tai khoan Admin
ham_surf_face(filePath)
