#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from random import randint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def user_invitation_code():
    codes = []
    codes.append('k23154415')  ## works for kkkk1123 - app nana user

    return codes

def google_password():
    pas = '158158123123'
    passwords = []
    passwords.append(pas)   ## for dilanhilo59
    passwords.append(pas)   ## for everybody3456

    return passwords

def google_users():

    users = []
    # users.append('rikitiki145')
    # users.append('roey3092')
    # users.append('royhamster67')
    # users.append('adamnegris1')
    users.append('dilanhilo59')
    users.append('everybody3456')

    return users

def sentences(code):
    all = []
    index = 0

    code1 = 'Please enter my Invitation Code!! ITS:     ', code, "     Just please make sure you comment on this post your Invitation Code so I will know to enter your's -     ", code
    code2 = 'Enter my invitation code for more Nanas - 2500:     ', code, '     But you must make sure you have more than 15K Nanas'
    code3 = "'Please Put My Code And I Will Put your's in:     ", code
    code4 = 'Please help me get more nanas:     ', code, '     (and help yourself too, for each code you put in we both get 2500 Nanas )     ', code
    code5 = code,     ' please help me'
    code6 = code,     ' <3'

    all.append(code)
    all.append(code1)
    all.append(code2)
    all.append(code3)
    all.append(code4)
    all.append(code5)
    all.append(code6)

    index = randint(0, all.__len__())
    random_sentence = all[index]

    return random_sentence


def login(user, password):
    try:
        join_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='O0WRkf zZhnYe C0oVfc KNnOOe xRXSA']")))
        join_button.click()

        need_to_click = driver.find_element_by_xpath("//*[@class='whsOnd zHQkBf']")
        need_to_click.click()

        userName = driver.find_element_by_xpath("//input[@name='identifier']")
        userName.send_keys(user)
        time.sleep(1)

        nextt = driver.find_element_by_xpath("//*[@id='identifierNext']")
        nextt.click()
        time.sleep(5)

        passwordd = driver.find_element_by_xpath("//*[@class='whsOnd zHQkBf']")
        passwordd.send_keys(password)
        time.sleep(1)

        nextt = driver.find_element_by_xpath("//*[@id='passwordNext']")
        nextt.click()

        print 'Site Reached: ', driver.title

        # join_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='O0WRkf oG5Srb C0oVfc KNnOOe xQl6Gb']")))
        # join_button.click()

        time.sleep(3)

        print 'Logged in to: ', user

    except:
        pass


def upload_code(invitation_code):
        try:
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='What would you like to share?']")))
            search_box.click()
            time.sleep(3)
            print 'Site Reached: ', driver.title

            text_zone = driver.find_element_by_tag_name('textarea')
            description = sentences(invitation_code)
            text_zone.send_keys(description)
            print 'The Description Printed:', description
            time.sleep(1)

            publish = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Post']")))
            publish.click()

            time.sleep(1)

            share = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-name='Share my code']")))
            share.click()

            print 'Code Uploaded to:', driver.title
            time.sleep(2)


        except:
            pass
            text_zone.clear()
            driver.refresh()



GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"/app/.chromedriver/bin/chromedriver"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.maximize_window()

google_plus_url = 'https://plus.google.com/communities/111173415890026985501'

driver.get(google_plus_url)
print 'Site Reached: ', driver.title

login('everybody3456', '158158123123')

while True:

    Codes = user_invitation_code()

    code = Codes.pop()

    driver.get(google_plus_url)
    print 'Site Reached: ', driver.title

    upload_code(code)

    print 'Waiting For The Next Account...'
    time.sleep(2700)  ## DEPENDS ON HOW MANY USERS YOU HAVE - 45 min per upload







        
  
