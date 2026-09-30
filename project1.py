from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

username = os.getenv("NSYSU_USERNAME")
password = os.getenv("NSYSU_PASSWORD")
driver=webdriver.Chrome()
driver.get("https://identity.nsysu.edu.tw/auth/realms/nsysu/protocol/cas/login?ui_locales=zh-TW&service=https%3A//elearn.nsysu.edu.tw/login%3Fnext%3D/user/index&locale=zh_TW&ts=1790599425.572905")
driver.maximize_window()
print("已進入登入頁面，準備登入...")
time.sleep(3)
username_input=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys(username)
password_input=driver.find_element(By.ID, "password")
password_input.send_keys(password)
login_btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']")))
login_btn.click()
print("登入成功")

driver.get("https://elearn.nsysu.edu.tw/course/37812/enrollments#/")
print("進入班級成員列表...")


name_list=[]
number_list=[]

def get_students(name_list,number_list):
    student_names=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[ng-bind='u.name']")))
    
    for student_name in student_names:
        name_list.append(student_name.text)

    student_numbers=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[ng-bind='u.user_no']")))
    
    for student_number in student_numbers:
        number_list.append(student_number.text)

    return name_list,number_list


while True:

    name_list,number_list=get_students(name_list,number_list)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    next_page_btn=driver.find_element(By.CSS_SELECTOR,"li.next-page-button a")

    if not next_page_btn.is_displayed():
        print("網頁已是最後一頁")
        break


    driver.execute_script("arguments[0].click();", next_page_btn)
    print("進入下一頁")

    time.sleep(3)


if len(name_list)==len(number_list):
    print("姓名跟學號數量一致")

df1=pd.DataFrame({
    "姓名":name_list ,
    "學號":number_list
})

df1=df1.iloc[2:]

df1.to_excel("project1.xlsx",index=False,sheet_name="行銷管理課程名單")
print("excel已建立")

















