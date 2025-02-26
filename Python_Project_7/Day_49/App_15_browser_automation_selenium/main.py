from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomation:
    def __init__(self):
        # Define driver, options, and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def Login(self, username, password):
        # Open the browser and go to the website
        self.driver.get('http://the-internet.herokuapp.com/login')

        # Locate the username and password fields, and login button
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'username'))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        login_button = self.driver.find_element(
            By.XPATH, '//*[@id="login"]/button'
        )

        # Fill in the username and password, and click the login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)
        # Locate the Elemental Selenium link and click it
        elements_selenium_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="page-footer"]/div/div/a')
            )
        )
        elements_selenium_link.click()

    def OpenSecondWebpage(self):
        # Wait for the new tab to open and switch to it
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Open the second webpage and perform actions
        self.driver.get('https://elementalselenium.com/')

    def fill_out_email_form(self, email, language):
        # Locate the email input field
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )

        # Locate programming language dropdown and Python option
        language_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'options'))
        )
        # Perform any additional actions on the second webpage
        # For this example, we will fill in the email field and select Python
        # from the dropdown and select send submit test pro tip button
        email_field.send_keys(email)
        language_dropdown.send_keys(language)

        # Locate and click the submit button
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 ('//*[@id="__docusaurus_skipToContent_fallback"]\
                  /main/div/div/div[1]/div/div/form/input[2]'))
            )
        )
        submit_button.click()

    def close_browser(self):
        # Wait for user input to close the browser
        self.driver.quit()


if __name__ == "__main__":
    Webautomation = WebAutomation()
    Webautomation.Login('tomsmith', 'SuperSecretPassword!')
    Webautomation.OpenSecondWebpage()
    Webautomation.fill_out_email_form("jlovlov23@gmail.com", "Python")
    Webautomation.close_browser()
