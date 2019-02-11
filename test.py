from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=996x829')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(3)
driver.get('http://13.124.52.157/screensharingtest.html')

driver.find_element_by_id('start').click()
driver.find_element_by_id('roomid').click()
driver.find_element_by_id('roomid').send_keys('2499806332950512')
driver.find_element_by_id('join').click()
