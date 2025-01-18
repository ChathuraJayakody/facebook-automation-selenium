from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookLogin:
    def __init__(self, driver_path, email, password):
        # Initialize driver and login credentials
        self.driver_path = driver_path
        self.email = email
        self.password = password
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        # Maximize window
        self.driver.maximize_window()
        
        # Open Facebook's login page
        self.driver.get("https://web.facebook.com/")
        time.sleep(5)  # Wait for 5 seconds to allow the page to load
        
        # Find the email input field and enter the email address
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(self.email)
        time.sleep(1)  # Wait for 1 second
        
        # Find the password input field and enter the password
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(self.password)
        time.sleep(1)  # Wait for 1 second
        
        # Find the login button and click it to log in
        self.driver.find_element(By.NAME, "login").click()
        
        # Wait until the 'Search Facebook' input field is present in the DOM
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Facebook']")))
        time.sleep(2)  # Pause the script for 2 seconds

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
        self.driver.quit()
