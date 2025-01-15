import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import demo as de
import os

# Retrieve phone number from environment variable or use a default placeholder
Mobile_number = os.getenv('MOBILE_NUMBER', 'YourDefaultNumber')  # Ensure sensitive data isn't hard-coded

# URLs for login page and test section
login_page_link = "https://live.impetusgurukul.com/store/course/368822/0?section=content"
Test_Section_link = "https://live.impetusgurukul.com/store/course/337549/19938077?section=content&parentId=368822&parentFolderId=0"

# Configure Edge browser options
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")  # Start browser maximized
options.add_experimental_option("detach", True)  # Keep browser open after script finishes
browser = webdriver.Edge(options=options)

# Function to open the login page and perform login
def openAndLogin(link, driver):
    """
    Navigates to the specified login link and performs the login operation using a mobile number.
    """
    driver.get(link)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(Mobile_number)
    time.sleep(5)  # Wait for page elements to load
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/button').click()
    time.sleep(5)  # Wait for the login process
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/button[2]')))
    button.click()  # Click on the next button after login

# Function to navigate to the test tab and perform actions based on the mock number
def Test_Tab(driver, MockNumber):
    """
    Navigates to the test section and interacts with elements based on the provided mock number.
    """
    time.sleep(20)  # Allow time for the page to load fully
    driver.get(Test_Section_link)
    time.sleep(25)  # Ensure all elements are loaded
    driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[{int(MockNumber)}]/div/a/div/div[2]/div/div/div[3]').click()
    de.Sectional_Summary(driver, mock_number=MockNumber)  # Call external function to handle additional actions

# Calling the openAndLogin function to perform login
openAndLogin(link=login_page_link, driver=browser)


# Loop to perform actions for multiple mock tests
for i in range(23, 57):
    Test_Tab(driver=browser, MockNumber=i)
    time.sleep(5)  # Pause between iterations to avoid overloading the server

# Close the browser once all actions are complete
browser.quit()
