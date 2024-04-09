import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import demo as de
#variable
# Mock_num = int(input("Enter mock:"))
Mobile_number ='9309497759'#"9325732481"#'9309497759'
login_page_link = "https://live.impetusgurukul.com/store/course/368822/0?section=content"
Test_Section_link ="https://live.impetusgurukul.com/store/course/337549/19938077?section=content&parentId=368822&parentFolderId=0"
'https://live.impetusgurukul.com/store/course/337549/19938077?section=content&parentId=368822&parentFolderId=0'
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)
# open website
def openAndLogin(link,driver):

    driver.get(link)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(Mobile_number)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/button').click()
    time.sleep(5)
    # driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/button[2]').click()
    button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/button[2]')))
    button.click()


def Test_Tab(driver,MockNumber):
    time.sleep(20)
    driver.get(Test_Section_link)
    time.sleep(25)
    driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[{int(MockNumber)}]/div/a/div/div[2]/div/div/div[3]').click()
    de.Sectional_Summary(driver,mock_number=MockNumber)

                   # -----------------------###############---------------------

##Calling all Function or Method

openAndLogin(link=login_page_link, driver=browser)
for  i in range(1,25):
    Test_Tab(driver=browser,MockNumber=i)
    time.sleep(5)

browser.quit()