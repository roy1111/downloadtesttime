#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def handle_Exception():
    try:
        publish_button = driver.find_element_by_xpath('//*[@class="_2ph- _4-u3"]')
        publish_button.click()

    except Exception as e:
        print e
        driver.refresh()
        pass


def kill_black_screen():
    try:
        black_screen = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_3ixn')))
        time.sleep(2)
        black_screen.click()

    except Exception as e:
        print e
        pass


def login(user, password):
    driver.find_element_by_xpath("//input[@name='email']").send_keys(user)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='pass']").send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('loginbutton').click()


def upload_code(groups, code):

    while True:
        for group in groups:
            try:
                driver.get(group)
                kill_black_screen()
                print 'Site Reached: ', driver.title

                ## TYPES THE CODE AND PUBLISHES IT
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, 0)")
                time.sleep(5)
                text_box = driver.find_element_by_xpath('//*[@class="_4h98 navigationFocus"]')

                # SCROLLS TO ELEMENT
                driver.execute_script("arguments[0].focus();", text_box)

                text_box.send_keys(code)

                kill_black_screen()

                publish_button = driver.find_element_by_xpath('//*[@class="_332r"]')
                publish_button.click()
                time.sleep(20)
                print 'The Code', code, 'Had Been Published'

            except Exception as e:
                print e
                handle_Exception()
                pass

        time.sleep(7120)  ## PUBLISH CODE EVERY TWO HOURS



Urlist = [
    'https://www.facebook.com/groups/712770162173432/?multi_permalinks=1373092012807907&notif_t=group_highlights&notif_id=1502070433060853',
    'https://www.facebook.com/groups/AppNanaFreeGiftCardsCashRewardInvitationCodes/',
    'https://www.facebook.com/groups/712770162173432/?ref=notif&notif_t=group_r2j_approved&notif_id=1501801308359145',
    'https://www.facebook.com/pg/App-Nana-Code-Trade-1375086212749266/posts/?ref=page_internal',
    'https://www.facebook.com/groups/1446945158905624/?ref=notif&notif_t=group_r2j_approved&notif_id=1501817930343661',
    'https://www.facebook.com/groups/438660146271847/?ref=notif&notif_t=group_r2j_approved&notif_id=1501866245589983']

Facebook_User_Name = 'royhamster67@gmail.com'
Facebook_User_Password = '158158123'
Code = 'K23154415'
GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH  = r"/app/.chromedriver/bin/chromedriver"
while True:
    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get('https://www.facebook.com/login')
    print 'Site Reached: ', driver.title

    login(Facebook_User_Name, Facebook_User_Password)
    print 'Site Reached: ', driver.title

    upload_code(Urlist, Code)
