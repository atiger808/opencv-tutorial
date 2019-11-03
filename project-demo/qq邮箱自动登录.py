# _*_ coding: utf-8 _*_
# @Time     : 2019/8/31 13:45
# @Author   : Ole211
# @Site     : 
# @File     : qq邮箱自动登录.py    
# @Software : PyCharm
# _*_ coding: utf-8 _*_
# @Time     : 2019/4/25 23:44
# @Author   : Ole211
# @Site     :
# @File     : qq_login.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://mail.qq.com/cgi-bin/loginpage'

driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

def qq_login(url):
    driver.get(url)
    form = driver.find_element_by_id('loginform')
    driver.switch_to.frame('login_frame')
    user = driver.find_element_by_id('u')
    user.clear()
    user.send_keys('594542251')
    password = driver.find_element_by_id('p')
    password.clear()
    password.send_keys('poo..14755')
    time.sleep(3)
    driver.find_element_by_id('login_button').click()
    time.sleep(3)
    driver.find_element_by_partial_link_text('收件箱').click()

qq_login(url)