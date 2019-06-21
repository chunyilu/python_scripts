# !/usr/bin/python
# coding:utf-8 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# logname = 'D:\\User profiles\\atgames\\Downloads\\selenium\\log\\%s.txt' % time.strftime('%Y%m%d%H%M%S')  # logname = 'testlog_' + date.today().isoformat() + '.log'
logname = 'G:\\selenium_log\\%s.txt' % time.strftime('%Y%m%d%H%M%S')  # logname = 'testlog_' + date.today().isoformat() + '.log'
logfile = open(logname, 'x')
logfile.writelines("D2d Purchase Process : " + time.strftime('%Y%m%d %X') + " \n")

website = "https://d2d-qa.direct2drive.com/#!/pc" #qa=https://d2d-qa.direct2drive.com/#!/pc      live=https://www.direct2drive.com/#!/pc
account = "lf210000@hotmail.com" #qa=lf210000@hotmail.com    live=joyce.huang@atgames.net
password = "Joyce7533"
name = "joyce002" #qa=joyce002        live=Joyce Huang
gamename = "nba 2k" #"Black Mirror" "qwer" "The Guild 2" "nba" "The Guild 2 Gold Edition"


#Open web
browser = webdriver.Chrome()
browser.get(website)
browser.maximize_window() #For maximizing window
browser.implicitly_wait(20) #gives an implicit wait for 20 seconds

#log
def log(txt, screen):
    print(txt + "\n")
    logfile.writelines(txt + "\n")
    if screen == 1:
        screenshot()

def screenshot():
    fileName = '%s' % time.strftime('%Y%m%d%H%M%S')
    browser.save_screenshot("D:\\User profiles\\atgames\\Downloads\\selenium\\log\\screenshot"+ fileName + ".png")
    log("screen" + fileName + ".png",0)

def D2D_login():
#Click login button
    login = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=user-panel]")))
    login.click()

    #time.sleep(4)
    #browser.switch_to_frame("")#browser.switch_to_window(browser.window_handles[1])
    #user = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/button") #browser.find_element_by_name("close")
    #user.click()
    #'''browser.switch_to_window(browser.window_handles[1])
    #for handle in browser.window_handles:
    #    browser.switch_to_window(handle)

#User_credential
    user_account = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "loginEmail"))) #user_account = browser.find_element_by_xpath("//*[@id='loginEmail']")
    user_account.send_keys(account)
    user_password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "loginPassword"))) #user_password = browser.find_element_by_xpath("//*[@id='loginPassword']")
    user_password.send_keys(password)


#Click login button
    login = browser.find_element_by_xpath( "//*[@id='login']/div[2]/form[1]/div[2]/div[3]/button")
    login.click()
    time.sleep(6)

#Check login success or not
    Verify_login= browser.find_element_by_xpath("//*[@id='navMenu']/li[2]/div/div/a/strong").text
    if Verify_login == name:
        log("Login Success", 0)
    else:
        log("Login Fail", 0)
        log("Login name  =  " + Verify_login, 0)

def check_shoppingcart():
    cart = []
    cart = browser.find_element_by_xpath("//*[@id='popover-cart']/button/span")#browser.find_elements_by_css_selector("#popover-cart > button > span")
    #cart_content = cart.text
    #cart_list = cart_content.split("\n")
    time.sleep(5)
    for ii in cart:
       print(ii.get_attribute('span'))

def Game_information():
#Search_product
    search_pc_store = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[1]/div/ul[3]/li/form/div/input") #Enter game name
    search_pc_store.send_keys(gamename) #zombie pinball #black mirror #Black Mirror
    log("Search game name : " + gamename, 0 )
    time.sleep(4)

    test = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[1]/div/ul[3]/li/form/div/ul") #搜尋form的內容，並列為list，方便查詢有幾個數量
    form_content = test.text
    form_list = form_content.split("\n") #用空白分開並存成list格式
    form_num = len(form_list) - 1 #-1是去掉搜尋game name的部分
    print(form_list) #list 內容
    log("Search form number : " + str(len(form_list)), 0) #數量

    time.sleep(1)

    flag = False
    if form_num == 0: #form沒有任何內容
        search_button= browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/ul[2]/li/form/div/button") #Press search button
        search_button.click()
        time.sleep(1)
        Verify_exist_game = browser.find_element_by_xpath("/ html / body / div[2] / div / div / div[2] / div / div / div[2] / div / div[3] / h2").text #No games found!  #qa="/ html / body / div[2] / div / div / div[2] / div / div / div[2] / div / div[3] / h2"    live="/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div[3]"
        if Verify_exist_game.strip() == "No Games Found!" or "No games found!":#Game information
            log("No match any game!", 0)
    else: #form有搜尋到內容，接著做比對
        for n in range(form_num):
            n += 1
            game_name_content = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[1]/div/ul[3]/li/form/div/ul/li[ " + str(n + 1) + "]/a") #第一個不算所以+1
            print(game_name_content.text)
            if gamename.lower() == game_name_content.text.lower(): #比對成功直接click進入頁面
                flag = True
                log("Search game name : " + gamename + "; Find the same game name : " + game_name_content.text, 0)
                game_name_content.click() #click進入頁面
                time.sleep(5) #等網頁跑完
                log("Game information screenshot : ", 1) #順帶screenshot game information page
            else:
                log("Search game name : " + gamename + "; Find the different game name : " + game_name_content.text, 0)
    if flag == False:
        log("No games found!", 1)


    ##Verify_exist_game = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div[3]").text #No games found!
    ##if Verify_exist_game.strip() == "No games found!":#Game information
    ##    log("No games found!")

    #game_information = browser.find_element_by_xpath(" //*[@id='5011475']/div[2]/div/h4")
    #game_information.click()

#Buy-put game to shopping cart
    if flag == True: #
        game_information = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/button") #press buy now -> put game to shopping cart
        game_information.click()
        log("Put game to shopping cart ", 0)



        shopping_cart = browser.find_element_by_xpath("//*[@id='popover-cart']/button/i") #enter shopping cart
        shopping_cart.click()
        log("Going to shopping cart ", 0)
        confirm_game = browser.find_element_by_xpath("//*[@id='cart-view-content']/div[3]/div[1]/div[1]/div[2]").text
        if gamename.lower() == confirm_game.lower():
            log("Put " + gamename + " to shopping cart success", 1)
        else:
            log("Put " + gamename + " to shopping cart fail", 1)

        checkout = browser.find_element_by_xpath("//*[@id='cart-view-content']/div[5]/div[1]/div[2]/div[2]/button[3]") #preceed checkout button
        checkout.click()
        time.sleep(7)

        #Paypal
        try:
            browser.switch_to.frame("paywallFrame") #切換到frame
            ##payment_method = browser.find_element_by_css_selector("body > ui-view > x-desktop-ctrl > div > fixed-layout > fixed-layout-content > div:nth-child(1) > desktopliststate > fixed-layout-scrollable > section > div.ui-content > x-payment-list > div:nth-child(2) > div.payment-items-area > div.payment-list-block.payment-list-block__buttons > div.payment-methods-list > div:nth-child(1) > div.payment-method-image > img")
            ##payment_method.click()
            time.sleep(5)
            log("Press Paypal mdthod to pay", 1)
            browser.switch_to.default_content()  # 定位切換回原網頁
        except Exception as e:
            log("No Paypal")


        #Pay now
        try:
            browser.switch_to.frame("paywallFrame") #切換到frame
            ##pay_now = browser.find_element_by_xpath("/html/body/ui-view/x-desktop-ctrl/div/fixed-layout/fixed-layout-content/div[1]/x-desktop-payment-state/fixed-layout-scrollable/div/section/div[1]/div/div/x-form-navigation/div[2]/div[2]/button")
            ##pay_now.click()
            log("Press Pay now", 1)
            browser.switch_to.default_content()  # 定位切換回原網頁
        except Exception as e:
            log("No Pay now")

        #Pay now confirm
        try:
            browser.switch_to.frame("paywallFrame") #切換到frame
            ##pay_now_confirm = browser.find_element_by_xpath("/html/body/ui-view/x-desktop-ctrl/div/fixed-layout/fixed-layout-content/div[1]/x-desktop-payment-state/fixed-layout-scrollable/div/section/div[1]/div/div/x-form-navigation/div[2]/div/button")
            ##pay_now_confirm.click()
            log("Press Pay now confrim", 1)
            browser.switch_to.default_content()  # 定位切換回原網頁
        except Exception as e:
            log("No Pay now confrim")

        time.sleep(5)
        log("Purchase success", 1)

D2D_login()
#check_shoppingcart()
Game_information()