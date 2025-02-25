from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Open the browser and go to the website
driver.get('http://the-internet.herokuapp.com/login')

# Locate the username and password fields, and login button
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'username'))
)
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'password'))
)
login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button')

# Fill in the username and password, and click the login button
username_field.send_keys('tomsmith')
password_field.send_keys('SuperSecretPassword!')
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elemental Selenium link and click it
elements_selenium_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    )
)
elements_selenium_link.click()

# Wait for the new tab to open and switch to it
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

# Open the second webpage and perform actions
driver.get('https://elementalselenium.com/')

# Locate the email input field
email_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'email'))
)

# Locate programming language dropdown and Python option
language_dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'options'))
)
# Perform any additional actions on the second webpage
# For this example, we will fill in the email field and select Python
# from the dropdown and select send submit test pro tip button
email_field.send_keys('jlovlov23@gmail.com')
language_dropdown.send_keys('Python')

# Locate and click the submit button
submit_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH,
         ('//*[@id="__docusaurus_skipToContent_fallback"]\
          /main/div/div/div[1]/div/div/form/input[2]'))
    )
)
submit_button.click()

# Wait for user input to close the browser
input("Press Enter to close the browser")
driver.quit()
