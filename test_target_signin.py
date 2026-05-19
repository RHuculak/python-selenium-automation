from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(3)

account_button = driver.find_element(By.ID, "account-sign-in")
account_button.click()
sleep(4)

signin_button = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
signin_button.click()
sleep(3)

text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']")
signin_button = driver.find_element(By.XPATH, "//button[text()='Continue']")
signin_button = driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']")

print('Test Passed')
# populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('table')

# wait for 4 sec


# click search button
# driver.find_element(By.NAME, 'btnK').click()

# verify search results
# assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')

driver.quit()
