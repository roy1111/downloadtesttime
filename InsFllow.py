#!/usr/bin/python2.7
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
    # driver.save_screenshot('screenie.png')

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


def enterCelebrityAccountFollowers(url):
    ## GOES TO THE CELEBRITY ACCOUNT
    driver.get(url)

    ## ENTERS CELEBRITY ACCOUNT FOLLOWERS
    Followers_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
    Followers_button.click()
    print (driver.title).encode('utf-8')


def getInsideSomeAccount(index):
    ## ENTERS THE ACCOUNT PROFILE AND WAITS FOR ALL PROFILES TO LOAD - THEN CLICKS ON PROFILE BY INDEX
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_6e4x5')))  ##ELEMENT NEEDS CHANGE* FINDS ALL LIST ITEMS
    Profile = WebDriverWait(driver, 5) \
        .until(EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2g7d5 notranslate _o5iw8']")))[
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
    now = time.time()

    while True:
        getInsideSomeAccount(index)
        time.sleep(3)
        print ("Site At Profile: ", driver.title.encode('utf-8'))

        try:
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE ELEMENT IS AVAILABLE
            PostAmount = driver.find_element_by_class_name('_fd86t').text
            print ('Number Of Posts: ', PostAmount)

            follow_button1 = driver.find_elements_by_xpath(
                "//button[contains(.,'Following')]")  ## NO NEED TO CHANGE ELEMENT
            follow_button2 = driver.find_elements_by_xpath(
                "//button[contains(.,'Requested')]")  ## NO NEED TO CHANGE ELEMENT

            ## CHECKS IF ACCOUNT HAS NOT ALREADY BEEN FOLLOWED
            if follow_button1.__len__() == 0 and follow_button2.__len__() == 0:

                after = time.time()

                if int(after) - int(now) > 90:
                    follow_button = driver.find_element_by_xpath(
                        "//button[contains(.,'Follow')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button.click()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))
                    AmountOfFectiveFollowed += 1
                    print ('Fictive Follow: ', AmountOfFectiveFollowed)
                    return AmountOfFectiveFollowed

                ## CHECKS IF ACCOUNT HAS MORE THAN 22 POSTS - IF DOES, FOLLOWED
                elif 40 <= int(PostAmount) < 151:
                    follow_button = driver.find_element_by_xpath(
                        "//button[contains(.,'Follow')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button.click()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[contains(.,'Following') or contains(.,'Requested')]")))
                    AmountOfActiveFollowed += 1
                    print ('Active Follow: ', AmountOfActiveFollowed)
                    enterCelebrityAccountFollowers(celebrityAccountURL)
                    after = time.time()
                    LoadingTime = waitUntilTimeReached(now, after, 91)
                    time.sleep(LoadingTime)
                    return AmountOfActiveFollowed

            ## IF, ONE OF THE IF'S STATEMENTS ARE FALSE, DRIVER GOES BACK TO LIST TO TRY NEXT ACCOUNT
            index += 1

            ## AFTER 20 PROFILES, LIST INDEX WILL BE OUT OF RANGE, SO THIS WILL HANDLE
            if index > 19:
                index = 0
                enterCelebrityAccountFollowers(celebrityAccountURL)

            else:
                driver.back()

        except Exception as e:  ## THE TRY AND CATCH WERE MADE FOR CONDITION TO KNOW THE PICTURE DATE (IF IT HAD BEEN UPLOADED LATELY)
            print (e)
            enterCelebrityAccountFollowers(celebrityAccountURL)
            return 0
            pass


username = 'onpoint_facts'
password = '158158123123'
celebrityAccountURL = 'https://www.instagram.com/luissuarez9/'

SumFollowesToday = 0
CounterUntilOneDay = 0

GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH  = r"/app/.chromedriver/bin/chromedriver"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.maximize_window()

loginToAccount(username, password)
enterCelebrityAccountFollowers(celebrityAccountURL)

while True:
    for x in range(0, 40):
        SumFollowesToday += followActiveAccount()

    ## CHECKS IF 24 HOURS HAD PASSED - SUPPOSED TO PRINT 960 FOLLOWERS
    CounterUntilOneDay += 1
    if CounterUntilOneDay == 24:
        print ('NUMBER OF FOLLOWES DONE TODAY: ', SumFollowesToday)
        CounterUntilOneDay = 0
        SumFollowesToday = 0
