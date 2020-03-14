from selenium import webdriver
################################ no load image #######################################
chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe', options = chrome_options)
#######################################################################################
driver.get('https://www.google.com')