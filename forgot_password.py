from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FacebookForgotPassword:
    def __init__(self, driver_path, email, google_password):
        # Initialize driver and credentials
        self.driver_path = driver_path
        self.email = email
        self.google_password = google_password
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def forgot_password(self):
        # Maximize window
        self.driver.maximize_window()
        
        # Open Facebook's login page
        self.driver.get("https://web.facebook.com/")
        time.sleep(5)
        
        # Find the email input field and enter the email address
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(self.email)
        time.sleep(1)
        
        # Click on the "Forgotten password?" link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Forgotten password?']").click()
        time.sleep(3)

        # Enter the email address in the recovery form
        self.driver.find_element(By.XPATH, "//input[@id='identify_email']").send_keys("seleniumtest.cinec@gmail.com")
        time.sleep(1)  # Wait for 1 second

        # Click on the "Search" button to submit the email
        self.driver.find_element(By.ID, "did_submit").click()
        time.sleep(3)  # Wait for 3 seconds
        
        # Click on "Try another way" link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Try another way']").click()
        time.sleep(3)
        
        # Select the option to send the recovery code via email
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Send code via email']").click()
        time.sleep(1)
        
        # Click on the "Continue" button to proceed
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        time.sleep(3)

        # Switch to Google tab for Gmail
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Open Google's homepage
        self.driver.get("https://www.google.com/")
        time.sleep(5)

        # Sign in to Google account
        self.driver.find_element(By.XPATH, "//a[@aria-label='Sign in']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='identifierId']").send_keys(self.email)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(self.google_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)

        # Open Gmail and search for the recovery code
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Gmail']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search mail']").send_keys("recovery code")
        time.sleep(2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        
        # Use PyAutoGUI to extract and copy the code
        pyautogui.moveTo(518, 308, duration=1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(591, 586, duration=1)
        pyautogui.doubleClick()
        time.sleep(1)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        time.sleep(2)

        # Switch back to the Facebook tab and paste the recovery code
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.find_element(By.ID, "recovery_code_entry").send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        time.sleep(4)
        
        # Skip further recovery steps
        self.driver.find_element(By.XPATH, "//button[@id='skip_button']").click()
        time.sleep(2)

        # Wait until the 'Search Facebook' input field is present in the DOM
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Facebook']")))
        time.sleep(3)

    def logout(self):
        # Find and click the menu (profile picture or other menu)
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(5) > div:nth-child(1) > span:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > g:nth-child(2) > image:nth-child(1)").click()
        time.sleep(2)  # Wait for 2 seconds
        
        # Find and click the logout button
        self.driver.find_element(By.CSS_SELECTOR, "div[data-nocookies='true'] i[class='x1b0d499 xep6ejk']").click()
        
        # Wait until the email input field is present again, indicating a successful logout
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        time.sleep(2)  # Pause the script for 2 seconds


    def close_browser(self):
        # Close the browser
        self.driver.quit()
