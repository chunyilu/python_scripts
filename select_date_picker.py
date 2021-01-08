import re
import os
import time
from selenium import webdriver
import string

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']


def date_picker(year, month, day):
    print(driver.find_element_by_xpath("(//*[@x-placement='bottom-start']//div)[5]").text)

    last_year_path = "(//*[@x-placement='bottom-start']//button)[1]"
    next_year_path = "(//*[@x-placement='bottom-start']//button)[3]"

    while True:
        left_date = driver.find_element_by_xpath("(//*[@x-placement='bottom-start']//div)[5]").text
        left_date_list = left_date.split()
        print(left_date_list[0])
        print(left_date_list[1])
        left_date_year = left_date_list[0]
        # left_date_month = left_date_list[1]

        if int(year) < int(left_date_year):
            driver.find_element_by_xpath(last_year_path).click()
        elif int(year) > int(left_date_year):
            driver.find_element_by_xpath(next_year_path).click()
        elif int(year) == int(left_date_year):
            break
        else:
            print("error handle")

    last_month_path = "(//*[@x-placement='bottom-start']//button)[2]"
    next_month_path = "(//*[@x-placement='bottom-start']//button)[4]"

    while True:
        left_date = driver.find_element_by_xpath("(//*[@x-placement='bottom-start']//div)[5]").text
        left_date_list = left_date.split()
        print(left_date_list[0])
        print(left_date_list[1])
        # left_date_year = left_date_list[0]
        left_date_month = left_date_list[1]
        # print(month)
        m_index = month_list.index(month)
        left_m_index = month_list.index(left_date_month)

        if m_index < left_m_index:
            driver.find_element_by_xpath(last_month_path).click()
        elif m_index > left_m_index:
            driver.find_element_by_xpath(next_month_path).click()
        elif m_index == left_m_index:
            break
        else:
            print("error handle")

    for x in range(1, 32):
        date = str(x)
        date_path = "(//*[@class='available']//span)[target_date]"
        new_path = date_path.replace("target_date", date)
        left_day = driver.find_element_by_xpath(new_path).text
        print(left_day)

        if str(day) == str(left_day):
            driver.find_element_by_xpath(new_path).click()
            print("day == left_day")
            break


driver = webdriver.Firefox()
driver.get("http://10.0.1.131:3001/en")
driver.maximize_window()
time.sleep(3)

username = driver.find_element_by_id("account")
username.send_keys("stev1604029627")

pwd = driver.find_element_by_id("password")
pwd.send_keys("123456")

#login
driver.find_element_by_xpath("//*[@class='login btn']").click()
time.sleep(6)

#report
driver.find_element_by_xpath("(//*[@class='left_bar']//div)[5]").click()
time.sleep(2)

#performance report
# driver.find_element_by_xpath("(//*[@class='left_bar']//li)[3]").click()
# time.sleep(2)

#member report
driver.find_element_by_xpath("(//*[@class='left_bar']//li)[5]").click()
time.sleep(2)

# driver.find_element_by_xpath("//*[@placeholder='Start date']").click()
# time.sleep(2)

driver.find_element_by_xpath("//*[@placeholder='start date']").click()
time.sleep(2)

date_picker(2017, "February", 1)
date_picker(2017, "February", 28)

