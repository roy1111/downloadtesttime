#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# from pyvirtualdisplay import Display
#
# # initiate virtual display
# display = Display(visible=0, size=(1080, 920))
# display.start()


def loginToAccount(UsrName, Password):
    ## GOES TO INSTAGRAM LOGIN PAGE
    driver.get('https://www.instagram.com/accounts/login/')
    print (driver.title).encode('utf-8')

    ## ENTERS THE USERNAME AND PASSWORD
    user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    user.send_keys(UsrName)
    time.sleep(1)
    passwordd = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    passwordd.send_keys(Password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(2)
    print (driver.title).encode('utf-8')
    
    ## DELETE AFTER
    codee = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='securityCode']")))
    codee.send_keys('073951')

    driver.get('https://www.instagram.com/accounts/login/')
    print driver.title.encode('utf-8')

    ## ENTERS THE USERNAME AND PASSWORD
    user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    user.send_keys(UsrName)
    time.sleep(1)
    passwordd = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    passwordd.send_keys(Password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(2)
    print driver.title.encode('utf-8')
    
    ## HANDLE SECURITY CHECK
    print (driver.current_url)
    try:
        permission = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'This Was Me')")))

        permission.click()

    except:
        pass


def enterCelebrityAccountFollowers(url):
    ## GOES TO THE CELEBRITY ACCOUNT
    driver.get(url)

    ## ENTERS CELEBRITY ACCOUNT FOLLOWERS
    Followers_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
    Followers_button.click()
    print (driver.title).encode('utf-8')


def getInsideSomeAccount(index):
    ## ENTERS THE ACCOUNT PROFILE AND WAITS FOR ALL PROFILES TO LOAD - THEN CLICKS ON PROFILE BY INDEX
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, '_6e4x5')))  ##ELEMENT NEEDS CHANGE* FINDS ALL LIST ITEMS
    Profile = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2g7d5 notranslate _o5iw8']")))[
        index]  ## ELEMENT NEEDS CHANGE

    Profile.click()


def waitUntilTimeReached(FirstTime, SecondTime, TimeDesiredToSleep):
    TimePassed = SecondTime - FirstTime
    SleepingTime = TimeDesiredToSleep - TimePassed

    if SleepingTime < 0:
        return 0

    else:
        return SleepingTime


def followActiveAccount():
    AmountOfActiveFollowed = 0
    AmountOfFectiveFollowed = 0
    index = 0
    FollowedUrList = []

    enterCelebrityAccountFollowers(celebrityAccountURL)
    getInsideSomeAccount(index)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE

    print ("Site At Profile: ") + driver.title.encode('utf-8')
    time.sleep(2)

    for y in range(0, 1):
        for x in range(0, 80): 

            follow_button = driver.find_element_by_xpath("//button[contains(.,'Follow')]")  ## NO NEED TO CHANGE ELEMENT
            
            FollowedUrList.append(driver.current_url)

            follow_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))
            
            now = time.time()

            enterCelebrityAccountFollowers(celebrityAccountURL)
            index = 0

            while True:

                try:
                    getInsideSomeAccount(index)
                    time.sleep(2)
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                                   '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE
                    print ("Site At Profile: ") + driver.title.encode('utf-8')

                    PostAmount = driver.find_element_by_class_name('_fd86t').text
                    print ('Number Of Posts: ') + PostAmount

                    follow_button1 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Following')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button2 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Requested')]")  ## NO NEED TO CHANGE ELEMENT

                    ## CHECKS IF ACCOUNT HAS NOT ALREADY BEEN FOLLOWED
                    if follow_button1.__len__() == 0 and follow_button2.__len__() == 0:

                        after = time.time()

                        if int(after) - int(now) > 44:  ##THERE IS A TIME.SLEEP FOR 2 SEC
                            AmountOfFectiveFollowed += 1
                            print ('Fictive Follow: ') + AmountOfFectiveFollowed
                            break

                        ## CHECKS IF ACCOUNT HAS MORE THAN 40 POSTS - IF DOES, FOLLOWED
                        elif 40 <= int(PostAmount) < 200:
                            print ('Active Follow: ') + AmountOfActiveFollowed
                            after = time.time()
                            LoadingTime = waitUntilTimeReached(now, after, 44)
                            time.sleep(LoadingTime)
                            AmountOfActiveFollowed += 1
                            break

                    ## IF, ONE OF THE IF'S STATEMENTS ARE FALSE, DRIVER GOES BACK TO LIST TO TRY NEXT ACCOUNT
                    index += 1

                    ## AFTER 20 PROFILES, LIST INDEX WILL BE OUT OF RANGE, SO THIS WILL HANDLE
                    if index > 19:
                        index = 0
                        enterCelebrityAccountFollowers(celebrityAccountURL)

                    else:
                        driver.back()

                except Exception as e:
                    print (e)
                    driver.back()
                    enterCelebrityAccountFollowers(celebrityAccountURL)

    print ("TODAY PROGRAM FOLLOWED: ") + FollowedUrList.__len__()
    return FollowedUrList


def Unfollow(FollowedUrList):
    Unfollowed = 1

    now = time.time()

    for url in FollowedUrList:
        try:
            driver.get(url)
                    
            Unfollow_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))
            
            after = time.time()

            LoadingTime = waitUntilTimeReached(now, after, 44)
            time.sleep(LoadingTime)

            Unfollow_button.click()

            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Follow')]")))
            
            now = time.time()

            Unfollowed += 1
            print ('Unfollowed ') + Unfollowed + ('accounts')

        except Exception as e:
            print (e)
            pass

    print ('UNFOLLOWED ACCOUNTS FOR TODAY:') + Unfollowed


username = 'onpoint_facts'
password = '158158123'
celebrityAccountURL = 'https://www.instagram.com/luissuarez9/'

GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"/app/.chromedriver/bin/chromedriver"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.maximize_window()

loginToAccount(username, password)

while True:
    Followed = followActiveAccount()
    Unfollow(Followed)
    break
  
