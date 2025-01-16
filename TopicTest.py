from selenium import webdriver
from selenium.webdriver.common.by import By
NewTopicTestLink="https://live.impetusgurukul.com/store/course/337549/21896001?section=content&parentId=368822&parentFolderId=0"
def TopicTest(driver):
    driver.get(NewTopicTestLink)
    for i in range(0,20):
        driver.find_element(By.XPATH,f"//*[@id='root']/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[{int(i)}]/div/a/div/div[2]/div/div/div[3]"
).click()
