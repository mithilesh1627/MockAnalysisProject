import time
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import os
import Screenshot
# dic = {"CorrectQuestion":[],
#        "InCorrectQuestion":[],
#        "UnAttemptedQuestion":[],
#        "TimeOnCorrectQuestion":[],
#        "TimeOnIncorrectQuestion":[],
#        "TimeOnUnattemptedQuestion":[]}



def Sectional_Summary(driver,mock_number):
    print("creating the respective file in folder")
    ImageFolder = f"E:/2024/Auto_Analysis/QuestionImage/Mock{mock_number}"
    ExcelFolder = f"E:/2024/Auto_Analysis/ExcelFile"
    os.mkdir(ImageFolder)
    DetailsTable = {}
    df = pd.DataFrame(DetailsTable)
    time.sleep(15)
    src=driver.find_element(By.XPATH,'/html/body/div[4]/div/div/iframe').get_attribute('src')
    driver.get(src)
    time.sleep(20)
    print("Analysis of Mock is started......")
    Total_Score = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[5]/div[1]/div[2]').text
    Accuracy = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[5]/div[1]/div[5]/div[2]/p').text.split(' ')[0]
    print(f"Total Score in Mock is : {Total_Score}, with the Accuracy of :{Accuracy}")
    SolutionLink = src.replace("reportSummary","solution")
    driver.get(SolutionLink)
    time.sleep(10)
    for i in range(1,121):
        status = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[3]/div[3]/span').text
        QuestionImage = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[4]')
        AnswerIamge = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[4]/div[5]')
        if status == "Correct":
            timeOnCorrect = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div[3]/div[3]/div[2]/span').text
            # dic["CorrectQuestion"].append(i)
            # dic["TimeOnCorrectQuestion"].append(timeOnCorrect)
            timeonquestion = timeOnCorrect
        elif status == "Incorrect":
            timeOnIncorrect = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[3]/div[3]/div[2]/span').text
            # dic["InCorrectQuestion"].append(i)
            # dic["TimeOnIncorrectQuestion"].append(timeOnIncorrect)
            timeonquestion =timeOnIncorrect
        else:
            timeOnUnattempted = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[3]/div[3]/div[1]/span').text
            # dic["UnAttemptedQuestion"].append(i)
            # dic["TimeOnUnattemptedQuestion"].append(timeOnUnattempted)
            timeonquestion = timeOnUnattempted
        QuestionImage.screenshot(f"{os.path.join(ImageFolder,str(i))}.png")
        # AnswerIamge.screenshot(f"{os.path.join(ImageFolder,f'Answer{str(i)}')}.png")
        # path=f"{os.path.join(ImageFolder,f'Answer{str(i)}')}"
        # Screenshot.GetIamge(QuestionImage,AnswerIamge,str(i),path=path)
        new_row = {'Question_no': i, 'Status': status, 'Spent_Time':
             datetime.strptime("00:"+str(timeonquestion), '%H:%M:%S').strftime('%H:%M:%S')}
        df = df._append(new_row, ignore_index=True)
        print(new_row)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div[5]/button[3]').click()
        time.sleep(1)
    df.to_excel(f"{ExcelFolder}/DetailsAnalysisOf{mock_number}.xlsx", index=False)