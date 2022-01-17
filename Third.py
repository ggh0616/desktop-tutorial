import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("disable-gpu") 
browser = webdriver.Chrome('chromedriver.exe', options=options)

url = "https://www.nyj.go.kr/rent"
time.sleep(1)
browser.get(url)
time.sleep(1)
browser.find_element_by_xpath("//*[@id='gnb']/ul/li[1]/a").click() #시설예약
time.sleep(1)

def Wallmoon(): #월문리 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[1]/a").click() #와부-조안 행정복지센터
    i = 3
    j = ['A', 'B', 'C', 'D', 'E']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 8:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def JangHyeon(): #장현배수지 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 1
    j = ['A', 'B', 'C', 'D']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[4]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Bupyeong(): #부평리 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 2
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[5]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Yangji(): #양지리 생활체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 1
    j = ['A', 'B', 'C', 'D']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[10]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Hwado(): #화도 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[3]/a").click() #화도-수동 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1   
    
def Bukhan(): #북한강 체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[3]/a").click() #화도-수동 행정복지센터
    i = 3
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1

def Toegye(): #퇴계원 체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[4]/a").click() #진건-퇴계원 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Jingun(): #진건공공하수처리시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[4]/a").click() #진건-퇴계원 행정복지센터
    i = 2
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[9]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Yakdae(): #약대울 체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[5]/a").click() #호평-평내 행정복지센터
    i = 3
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 6:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1
    
def Yanggol(): #양골마을체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[6]/a").click() #금곡-양정 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    time.sleep(0.5)

    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(j[k]+" 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
        k += 1           

def Jigeum(): #지금배수지
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
    time.sleep(0.5)
        
    while(True):
        if i == 7:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click() #코트A 
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0}번 코트 ".format(i))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2)) 
        i += 1
    
def Coat1(): #체육공원1호
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 2
    j = 1    
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[4]/a").click()
    time.sleep(0.5)
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click()
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0}번 코트 ".format(j))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2))    
        i += 1
        j += 1
        
def Coat2(): #체육공원2호
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click()
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0}번 코트 ".format(i))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2))    
        i += 1
        
def Gown(): #가운동 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[5]/a").click()
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{0}]/a".format(i)).click()
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0}번 코트 ".format(i))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2))   
        i += 1

def Puleun(): #가운푸른물센터 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터   
    i = 1    
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[7]/a").click()
    time.sleep(0.5)
    
    while(True):
        if i == 2:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li/a").click()
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0}번 코트 ".format(i))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2))  
        i += 1
    
def Gigu(): #별내택지지구체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[8]/a").click() #별내행정복지센터
    i = 2
    j = "E" 
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[1]/a").click()
    time.sleep(0.5)
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[2]/a").click()
        time.sleep(1)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0} 코트 ".format(j))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    print(ry+rm.zfill(2)+rd.zfill(2))  
        i += 1
    
def Gwang(): #별내전 광전리 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[8]/a").click() #별내행정복지센터
    i = 1
    j = "A"
    k = 1   
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    time.sleep(0.5)
    while(True):
        if i == 2:            
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li/a").click()
        time.sleep(1)
            
        soup = BeautifulSoup(browser.page_source, "lxml")
        time.sleep(1)
            
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print("{0} 코트 ".format(j))
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
                
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    zz = ina['alt']                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)    
                    print(ry+rm.zfill(2)+rd.zfill(2))     
        i += 1 
print("\n")       
        

print("월문리 생활체육시설")        
Wallmoon()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Wallmoon()

print("-----------------------")

print("장현배수지 생활체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
JangHyeon()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
JangHyeon()

print("-----------------------")

print("부평리 생활체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Bupyeong()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Bupyeong()

print("-----------------------")

print("양지리 생활체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Yangji()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Yangji()

print("-----------------------")

print("화도 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Hwado()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Hwado()

print("-----------------------")

print("북한강 체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Bukhan()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Bukhan()

print("-----------------------")

print("퇴계원 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Toegye()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Toegye()

print("-----------------------")

print("약대울 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Yakdae()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Yakdae()

print("-----------------------")

print("양공마을체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Yanggol()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Yanggol()

print("-----------------------")

print("진건공공하수처리시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Jingun()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Jingun()

print("-----------------------")
    
print("지금배수지 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
Jigeum()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Jigeum()

print("-----------------------")

print("체육공원1호 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Coat1()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Coat1()

print("-----------------------")

print("체육공원2호 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Coat2()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Coat2()

print("-----------------------")

print("가운동 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Gown()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Gown()

print("-----------------------")

print("가운푸른물센터 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Puleun()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Puleun()

print("-----------------------")

print("별내택지지구체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Gigu()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Gigu()

print("-----------------------")

print("별내면 광전리 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
Gwang()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
Gwang()