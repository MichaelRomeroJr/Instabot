# -*- coding: utf-8 -*-
""" Author: Michael Romero Jr """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, Engage, Login
from time import sleep
from random import randint

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=800,1000");
chrome_options.add_argument("--window-position=0,0");

driver = webdriver.Chrome('/Users/michaelromero/anaconda2/bin/chromedriver 4', chrome_options = chrome_options)

chrome_options = Options()
chrome_options.add_argument("--window-size=700,1000");
chrome_options.add_argument("--window-position=0,0");


def accountLogin(driver, username, password):
    driver.get("https://instagram.com/accounts/login")
    sleep(4)
       
    el=driver.find_elements_by_tag_name("a")[0]

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 500, 500)
    action.click()
    action.perform()
    
    driver.find_element_by_name('username').send_keys(username) 
    driver.find_element_by_name('password').send_keys(password)     
    buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]") #Click button by text
    buttons[0].click() #buttons is a list, so click first element    
    time.sleep(5)
    
    try: #Close the "Log in from App" Window
        driver.find_element_by_xpath("//button[@class='_dbnr9']").click()
    except:
        print("There was no 'Log in from App' popup")
    return


def EngageTargetAccounts(driver, username, password, targetAccount):
    num=1    
    driver.get('https://instagram.com/' + targetAccount)
    main_elem = driver.find_element_by_tag_name('main') # Get Links
    link_elems = main_elem.find_elements_by_tag_name('a')
    picsToLike = []
    media=None
    if media is None: #All kmedia types
        media = ['', 'Post', 'Video']
    elif media == 'Photo': #Posts w/ multiple pics
        media = ['', 'Post']
    else: #Make it a list
        media = [media]
    
    try:
        if link_elems:
            addLinks = [link_elem.get_attribute('href') for link_elem in link_elems if link_elem and link_elem.text in media] 
            picsToLike.extend(addLinks[:1])        
    except BaseException as e:
        print("link_elems error \n", str(e))  
    driver.get(picsToLike[0]) #Open the link of the recent photo
    driver.find_element_by_partial_link_text('likes').click() #Click to see who's liked it
    sleep(3)
    elemInsidePopUp = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/ul/div/li[1]/div/div[1]/div/div[1]/a")
    
    for i in range(25): #scroll through list of who I'm following
        elemInsidePopUp.send_keys(Keys.END)
        sleep(1)
    
    #div = driver.find_elements_by_class_name('_2nunc')
    div = driver.find_elements_by_class_name('NroHT')
    
    
    likers=[] 
    for i in div: #Get URL's of everyone that has 'liked' pic
        likers.append(i.find_element_by_css_selector('a').get_attribute('href'))
        
        
    picsToLike = []
    for account in likers:
        media1=None
        if media1 is None: #All kmedia types
            media1 = ['', 'Post', 'Video']
        elif media1 == 'Photo': #Posts w/ multiple pics
            media1 = ['', 'Post']
        else: #Make it a list
            media1 = [media]
        driver.get(account)   
        sleep(2)
          
        main_elem = driver.find_element_by_tag_name('main') # Get Links
        link_elems = main_elem.find_elements_by_tag_name('a')
        
        try:
            if link_elems:
                addLinks = [link_elem.get_attribute('href') for link_elem in link_elems if link_elem and link_elem.text in media1] 
                picsToLike.extend(addLinks[:6]) 
                
                accountPics = [link_elem.get_attribute('href') for link_elem in link_elems if link_elem and link_elem.text in media1] 
                pics=[]
                pics = accountPics[:5]
                
                for i in pics:
                    driver.get(i)
                    #likeElem = driver.find_elements_by_xpath("//a[@role='button']/span[text()='Like']/..")                    
                    likeElem = driver.find_elements_by_xpath("//button/span[text()='Like']")
                                            
                    if len(likeElem) == 1:
                        likeElem[0].click()
                        print('Liked: ', num)
                        num+=1
                        sleepTime = randint(5, 15)
                        sleep(sleepTime)
                    else:
                        print('Already liked or Not a Photo')   
                    if num>=300:
                        break

        except BaseException as e:
            print("link_elems error \n", str(e))
        
    return picsToLike[:300]      

def likeFromList(driver, list):
    num=1
    for i in list:a
        driver.get(i)
        like_elem = driver.find_elements_by_xpath("//a[@role='button']/span[text()='Like']/..")
        if len(like_elem) == 1:
            like_elem[0].click()
            print('Liked: ', num)
            num+=1
            sleepTime = randint(5, 10)
            sleep(sleepTime)
        else:
            print('Already liked or Not a Photo')
    driver.quit()

username = "hardcoded_username"
password = "hardcoded_password"
accountLogin(driver, username, password)
links = EngageTargetAccounts(driver, username, password, target) # return list of active user photos 
likeFromList(driver, links) # function that likes from a list of accounts 
