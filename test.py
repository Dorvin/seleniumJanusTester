from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=996x829')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(3)

for i in range(2,12):
	driver.get('http://13.124.52.157/screensharingtest.html')
	driver.find_element_by_id('start').click()
	driver.find_element_by_id('roomid').click()
	driver.find_element_by_id('roomid').send_keys('368101203117938')
	driver.find_element_by_id('join').click()
	driver.execute_script("window.open('about:blank'," + " '" + "tab" + str(i) + "');")
	driver.switch_to.window("tab"+str(i))
print('test is completed successfully')
