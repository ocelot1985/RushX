#coding=utf-8

# XiaoMi rushing tools
# Author: ZhangKai
# Email : ocelot1985@gmail.com

import time
from splinter import Browser

# Data area
USER = 'XXX'
PASS = 'XXX'


def Login(browser):
	browser.visit('http://order.mi.com/site/login?ac=1')
	time.sleep(2)
	browser.find_by_id('miniLogin_username').fill(USER)
	browser.find_by_id('miniLogin_pwd').fill(PASS)
	browser.find_by_id('message_LOGIN_IMMEDIATELY').click()
	time.sleep(2)

def getCookie(browser):
	cookie = browser.cookies.all()
	# print detail of cookies
	for i in cookie:
		print i
		for k in i:
			print "Key[%s] = "%k, i[k]
		print "====split===="

def clear(browser):
	browser.quit()


if __name__ == '__main__':
	browser = Browser()
	Login(browser)
	getCookie(browser)
	
	clear(browser)