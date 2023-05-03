from selenium import webdriver

url = '#PUT THE WEB URL'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('#TYPE XPATH OF THE ELEMENT TO SCRAP HERE').click()