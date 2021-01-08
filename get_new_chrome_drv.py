import requests
from selenium import webdriver
import zipfile

url = 'https://chromedriver.storage.googleapis.com/index.html?path='
url_file = 'https://chromedriver.storage.googleapis.com/'
ver_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'
file_name = 'chromedriver_win32.zip'

#get current browser chrome version
driver = webdriver.Chrome()
if 'browserVersion' in driver.capabilities:
    print(driver.capabilities['browserVersion'])
    version = driver.capabilities['browserVersion']
else:
    print(driver.capabilities['version'])
    version = driver.capabilities['version']
driver.quit()

#get first n characters
ver_tmp = ""
for i in range(9):
    ver_tmp = ver_tmp + version[i]

#get chrome driver version
version_response = requests.get(ver_url + ver_tmp)
version = version_response.text

#get chrome driver page
version_response = requests.get(url + version)
print(version_response)

if version_response.text:
    # get chrome driver
    file = requests.get(url_file + version + '/' + file_name)
    print(file)
    with open(file_name, "wb") as code:
        code.write(file.content)

#unzip file and overwrite chromedriver.exe
pz = open(file_name, 'rb')
packz = zipfile.ZipFile(pz)
for name in packz.namelist():
    packz.extract(name, 'C:/Python27/Scripts')
pz.close()