from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def openAndLogin(link,driver):
    Mobile_number = '9325732481'    #"9325732481"#'9309497759'
    driver.get(link)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div[1]/input').send_keys(Mobile_number)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/button').click()

    time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/button[2]').click()
    button = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/button[2]')))

    button.click()
