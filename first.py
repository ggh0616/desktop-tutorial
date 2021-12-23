import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = "https://www.ycs.or.kr/yeyak/fmcs/43"

browser.get(url)
court_click1 = browser.find_element_by_xpath("//*[@id='center']/option[6]").click() #센터
time.sleep(1)
court_click2 = browser.find_element_by_xpath("//*[@id='part']/option[1]").click() #시설
time.sleep(1)
court_click3 = browser.find_element_by_xpath("//*[@id='place']/option[3]").click() #장소
time.sleep(1)
browser.find_element_by_xpath("//*[@id='search']/fieldset/div/div/div/button").click() #선택
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")

info_calendar = soup.find("div", attrs={"class":"calendar"}).find("tbody").find_all("tr")

for cale in info_calendar:
    calen = cale.find_all("td")  
    print("일요일:", calen[0].get_text())        
    print("월요일:", calen[1].get_text())
    print("화요일:", calen[2].get_text())        
    print("수요일:", calen[3].get_text()) 
    print("목요일:", calen[4].get_text())        
    print("금요일:", calen[5].get_text()) 
    print("토요일:", calen[6].get_text()) 
    
time.sleep(1)

browser.find_element_by_xpath("//*[@id='date-20211230']").click()

can_tennis = soup.find("div", attrs={"class":"regist_list"}).find("tbody").find_all("tr")

for row in can_tennis:
    columns = row.find_all("td")
    
    if columns[0].get_text() == "-":
        print("회차:", columns[1].get_text())
        print("시간:", columns[2].get_text())   
        print("현재는 가능하지 않습니다.")     
    else:
        print("회차:", columns[1].get_text())
        print("시간:", columns[2].get_text())
        print("가능 여부:", columns[3].get_text())

time.sleep(2)
    
    
    

    
    