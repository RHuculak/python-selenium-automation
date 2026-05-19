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
# NOTE: Stack Overflow is protected by Cloudflare, so this might not work
driver.get('https://stackoverflow.com/users/signup')
sleep(4)

# Create your account element
create_account_elem = driver.find_element(By.XPATH, "//h1[text()='Create your account']")

# Terms of Service blurb
tos_elem = driver.find_element(By.CSS_SELECTOR, ".js-terms")

# Email input
email_input = driver.find_element(By.ID, "email")
email_input = driver.find_element(By.CSS_SELECTOR, "input#email")

# Password input
password_input = driver.find_element(By.ID, "password")
email_input = driver.find_element(By.CSS_SELECTOR, "input#password")

# Show Password icon
show_pass_icon = driver.find_element(By.CSS_SELECTOR, "svg.iconEyeOffSm")

# Sign Up Button
signup_button = driver.find_element(By.CSS_SELECTOR, "svg.iconEyeOffSm")
signup_button = driver.find_element(By.CSS_SELECTOR, "button[name='submit-button']")

# Sign Up with Google button
google_signup_button = driver.find_element(By.CSS_SELECTOR, "button.s-btn__google[data-provider='google']")

# Sign Up with Github button
github_signup_button = driver.find_element(By.CSS_SELECTOR, "button.s-btn__github[data-provider='github']")

# Get Stack Overflow for Teams link
teams_ad_link = driver.find_element(By.CSS_SELECTOR, "a[href*='https://stackoverflow.com/teams']")

print('Test Passed')

driver.quit()
