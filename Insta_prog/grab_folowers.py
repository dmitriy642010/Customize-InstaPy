from instapy import InstaPy
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.implicitly_wait(5)

session = InstaPy(username="YourUserName", password="YourPassword",bypass_security_challenge_using='sms')
session.login()
sleep(5)

"""This feature grabs followers of user"""
Test_grab = session.grab_followers(username="someone_1", amount='full', live_match=True, store_locally=True)

"""This feature grabs following of user"""
lazySmurf_following = session.grab_following(username="someone_2", amount='full', live_match=True, store_locally=True)

#After run it will show in terminal the path to a json file fith all grabbed users