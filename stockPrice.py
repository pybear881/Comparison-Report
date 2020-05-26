from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

stype = 'Equities'
number = ''
url = 'https://www.hkex.com.hk/Market-Data/Securities-Prices/{}/{}-Quote?sym={}&sc_lang=en'.format(stype,stype,number)
gecko = 'C:\\Python37\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=gecko)
driver.get(url)
time.sleep(5)
driver.minimize_window()

while True:
	try:
		price = driver.find_element_by_xpath("//span[@class='col_last']").text
		ct = str(datetime.now())
		print(ct.split('.')[0] + ' ==> ' + price)
		time.sleep(10)
		
	except Exception as e:
		raise e
