import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# time for pausing
#import time


# try:
# chrome_options allows the window to stay open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

# Open site
driver.get('https://chat.indystar.com/')


# Select the id/name box by assinging a variable to the driver
firstName_box = driver.find_element_by_name('chatFirstName')
# Send id box information
firstName_box.send_keys('Denise')

lastName_box = driver.find_element_by_name('chatLastName')
lastName_box.send_keys('Herhusky')

phone_box = driver.find_element_by_name('chatPhoneNumber')
phone_box.send_keys('3177557766')

email_box = driver.find_element_by_name('chatEmailAddress')
email_box.send_keys('dherhusky@gmail.com')


option_button = driver.find_element_by_id('inputGroupSubject')
option_button.click()
option_select = driver.find_element_by_xpath('//*[@id="inputGroupSubject"]/option[2]')
option_select.click()

# except:
#     print("An exception occurred")

        # return print("Success!")
