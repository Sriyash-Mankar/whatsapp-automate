import selenium
import time
from selenium import webdriver
c = webdriver.Chrome(executable_path='D:\chromedriver.exe')
c.get('https://web.whatsapp.com/')
time.sleep(10)
uname = 'Yashashree'
c.find_element_by_xpath('//span[@title="{}"]'.format(uname)).click()
c.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').click()
c.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("This is an automated text just testing my whabot")
c.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
ab = c.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span').click()
ib = c.find_element_by_class_name('wnDP3').click()
