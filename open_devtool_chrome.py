from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r'C:\Python27\Scripts\chromedriver.exe')
driver.get("http://10.0.1.131/")
print(driver.title)

login = driver.find_element_by_xpath("//*[@id='__layout']/div/div/div[1]/header/div/div[2]/div[2]/div[1]")
login.click()
