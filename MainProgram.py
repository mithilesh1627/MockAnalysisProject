import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Login as ec
import MockAnalysis as de
import TopicTest as tt

#variable
# Mock_num = int(input("Enter mock:"))
Mock_num = 51
login_page_link = "https://live.impetusgurukul.com/store/course/471292/21821943?section=content"
Mock_Section_link = "https://live.impetusgurukul.com/store/course/337549/19936932?section=content&parentId=471292&parentFolderId=21821943"
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)
# open website
def Test_Tab(driver,MockNumber):
    time.sleep(20)
    driver.get(Mock_Section_link)
    time.sleep(25)
    print(f"Starting the Analysis of Mock number {str(Mock_num)}")
    driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[{int(MockNumber)}]/div/a/div/div[2]/div/div/div[3]').click()
    de.Sectional_Summary(driver,mock_number=MockNumber)

                   # -----------------------###############---------------------

##Calling all Function or Method

ec.openAndLogin(link=login_page_link, driver=browser)
print("successfully login to website")
print("Switching to Mock Test Panel")
# Test_Tab(driver=browser,MockNumber=int(Mock_num))
for i in range(54,60):
    print(f"Started the Mock number {i}")
    Test_Tab(driver=browser,MockNumber=i)
    print(f"Completed the Mock number {i}")
    time.sleep(2)
print("you have been logout successfully")

##################################################################################

# Test_Tab(driver=browser,MockNumber=50)
# print("Moving to TopicWise Test Window")
# tt.TopicTest(driver=browser)
browser.quit()
