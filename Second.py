import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re

browser = webdriver.Chrome()

url = "https://www.ycs.or.kr/yeyak/fmcs/43"

browser.get(url)
browser.find_element_by_xpath("//*[@id='center']/option[6]").click() #센터
time.sleep(1)
browser.find_element_by_xpath("//*[@id='part']/option[1]").click() #시설
time.sleep(1)

i = 1

while (True):    
    if i == 14:
        break    
    court_click1 = browser.find_element_by_xpath("//*[@id='place']/option[{0}]".format(i)).click() #장소
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='search']/fieldset/div/div/div/button").click() #선택
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source, "lxml")        
    time.sleep(1)

    all_data = soup.find("div", attrs={"class":"calendar"}).find("div", attrs={"class":"align_box"}).find("tbody").find_all("tr")
    can_re = soup.find_all("td", attrs={"data-state_cd":"10"})
            
    print("코트: " + str(i) +"번")         
    for i_i in can_re:
        a_tag = i_i.select("a")[0]['id']
        fi_day = re.findall(r'\d+', a_tag)        
        print(fi_day)
            
    i += 1    
    
    time.sleep(1)  
    
time.sleep(1)    
