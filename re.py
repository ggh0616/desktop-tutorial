from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options
import pymysql 

conn = pymysql.connect(host='localhost', user='root', password='Rhksgjs@147', db='kwan', charset='utf8')
curs = conn.cursor()

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("disable-gpu") 
browser = webdriver.Chrome('chromedriver.exe', options=options)

url = "https://www.nyj.go.kr/rent"
browser.get(url)
browser.find_element_by_xpath("//*[@id='gnb']/ul/li[1]/a").click() #시설예약

curs.execute("""ALTER TABLE rese auto_increment = 1""") #id 값 1로 초기화
curs.execute("""SELECT DISTINCT rese_date, rese_name FROM rese""")

def wallmoon(): #월문리 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[1]/a").click() #와부-조안 행정복지센터
    i = 3
    j = ['A', 'B', 'C', 'D', 'E']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()

    while(True):
        if i == 8:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"월문리 생활체육시설 {j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)                    
                    fin = (ry+rm.zfill(2)+rd.zfill(2))
                    print(fin) 
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"월문리 생활체육시설 {j[k]}코트", fin])  
        i += 1
        k += 1
    
def jangHyeon(): #장현배수지 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 1
    j = ['A', 'B', 'C', 'D']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[4]/a").click()    
    
    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A         
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"장현배수지 생활체육시설 {j[k]} 코트")
        print("예약가능한 날짜")        
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2))
                    print(fin)                      
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"장현배수지 생활체육시설 {j[k]}코트", fin]) 
        i += 1
        k += 1
    
def bupyeong(): #부평리 생활체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 2
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[5]/a").click()    
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
       
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"부평리 생활체육시설 {j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2))
                    print(fin) 
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"부평리 생활체육시설 {j[k]}코트", fin])   
        i += 1
        k += 1
    
def yangji(): #양지리 생활체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[2]/a").click() #진접오남행정복지센터
    i = 1
    j = ['A', 'B', 'C', 'D']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[10]/a").click()
    
    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"양지리 생활체육공원 {j[k]} 코트")
        print("예약가능한 날짜") 
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"양지리 생활체육공원 {j[k]}코트", fin])    
        i += 1
        k += 1
    
def hwado(): #화도 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[3]/a").click() #화도-수동 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
     
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"화도 테니스장{j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"화도 테니스장 {j[k]}코트", fin]) 
        i += 1
        k += 1   
    
def bukhan(): #북한강 체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[3]/a").click() #화도-수동 행정복지센터
    i = 3
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    
    while(True):
        if i == 5:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"북한강 체육공원 {j[k]} 코트")
        print("예약가능한 날짜") 
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"북한강 체육공원 {j[k]}코트", fin])  
        i += 1
        k += 1

def toegye(): #퇴계원 체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[4]/a").click() #진건-퇴계원 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"퇴계원 체육시설 {j[k]} 코트")
        print("예약가능한 날짜") 
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":         
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"퇴계원 체육시설 {j[k]}코트", fin])   
        i += 1
        k += 1
    
def jingun(): #진건공공하수처리시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[4]/a").click() #진건-퇴계원 행정복지센터
    i = 2
    j = ['A', 'B']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[9]/a").click()
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"진건공공하수처리시설 {j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"진건공공하수처리시설 {j[k]}코트", fin])   
        i += 1
        k += 1
    
def yakdae(): #약대울 체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[5]/a").click() #호평-평내 행정복지센터
    i = 3
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
    
    while(True):
        if i == 6:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
         
        soup = BeautifulSoup(browser.page_source, "lxml")
         
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"약대울 체육시설 {j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":       
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"약대울 체육시설 {j[k]}코트", fin])   
        i += 1
        k += 1
    
def yanggol(): #양골마을체육시설
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[6]/a").click() #금곡-양정 행정복지센터
    i = 1
    j = ['A', 'B', 'C']
    k = 0
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"양골마을체육시설{j[k]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"양골마을체육시설 {j[k]}코트", fin])  
        i += 1
        k += 1           

def jigeum(): #지금배수지
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[2]/a").click()
        
    while(True):
        if i == 7:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click() #코트A 
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"지금배수지 {i}번 코트 ")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"지금배수지 {i}코트", fin])    
        i += 1
    
def coat1(): #체육공원1호
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 2
    j = 1
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[4]/a").click()
    
    while(True):
        if i == 4:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click()
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"체육공원1호 {i}번 코트 ")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"체육공원1호 {i}코트", fin])    
        i += 1
        j += 1
        
def coat2(): #체육공원2호
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click()         
        
        soup = BeautifulSoup(browser.page_source, "lxml")         
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"체육공원2호 {i}번 코트 ")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":            
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"체육공원2호 {i}코트", fin])    
        i += 1
        
def gown(): #가운동 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터
    i = 1
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[5]/a").click()
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath(f"//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[{i}]/a").click()         
        
        soup = BeautifulSoup(browser.page_source, "lxml")         
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"가운동 테니스장 {i}번 코트 ")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":               
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"가운동 테니스장 {i}코트", fin]) 
        i += 1

def puleun(): #가운푸른물센터 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[7]/a").click() #다산 행정복지센터   
    i = 1    
     
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[7]/a").click()
    
    while(True):
        if i == 2:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li/a").click()         
        
        soup = BeautifulSoup(browser.page_source, "lxml")         
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"가운푸른물센터 테니스장 {i}번 코트 ")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":          
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"가운푸른물센터 테니스장 {i}코트", fin])    
        i += 1
    
def gigu(): #별내택지지구체육공원
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[8]/a").click() #별내행정복지센터
    i = 2
    j = ['E']
     
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[1]/a").click()
    
    while(True):
        if i == 3:
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li[2]/a").click()
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"별내택지지구체육공원 {j[0]} 코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]
            tm = tr.select('span.blind')[1]
            td = tr.select('span.blind')[2]
            
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"별내택지지구체육공원 {j[0]}코트", fin])  
        i += 1
    
def gwang(): #별내전 광전리 테니스장
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[1]/li[8]/a").click() #별내행정복지센터
    i = 1
    j = ["A"]   
     
    browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[1]/ul/li[3]/a").click()
     
    while(True):
        if i == 2:            
            break
        browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[2]/li[2]/ul/li[2]/ul/li/a").click()         
            
        soup = BeautifulSoup(browser.page_source, "lxml")         
            
        w_no = soup.select("#contents > div.content_body > table > tbody > tr > td")
        print(f"별내전 광전리 테니스장 {j[0]}코트")
        print("예약가능한 날짜")
        for tr in w_no:        
            ty = tr.select('span.blind')[0]   
            tm = tr.select('span.blind')[1]   
            td = tr.select('span.blind')[2]   
                
            alt_n1 = tr.select('a img')        
            for ina in alt_n1:
                if ina['alt'] == "예약가능":                
                    ky = ','.join(repr(e) for e in ty)
                    km = ','.join(repr(e) for e in tm)
                    kd = ','.join(repr(e) for e in td)
                    ry = re.sub(r'[^0-9]', '', ky)
                    rm = re.sub(r'[^0-9]', '', km)
                    rd = re.sub(r'[^0-9]', '', kd)    
                    fin = (ry+rm.zfill(2)+rd.zfill(2)) 
                    print(fin)
                    sql = """INSERT INTO rese(rese_name, rese_date) VALUES (%s, %s)"""  
                    curs.execute(sql, [f"별내전 광전리 테니스장 {j[0]}코트", fin]) 
        i += 1

print("월문리 생활체육시설")        
wallmoon()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
wallmoon()

print("-----------------------")

print("장현배수지 생활체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
jangHyeon()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
jangHyeon()      

print("-----------------------")

print("부평리 생활체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
bupyeong()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
bupyeong()

print("-----------------------")

print("양지리 생활체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
yangji()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
yangji()

print("-----------------------")

print("화도 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
hwado()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
hwado()

print("-----------------------")

print("북한강 체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
bukhan()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
bukhan()

print("-----------------------")

print("퇴계원 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
toegye()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
toegye()

print("-----------------------")

print("약대울 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
yakdae()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
yakdae()

print("-----------------------")

print("양공마을체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
yanggol()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
yanggol()

print("-----------------------")

print("진건공공하수처리시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
jingun()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
jingun()

print("-----------------------")
    
print("지금배수지 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()        
jigeum()      
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
jigeum()

print("-----------------------")

print("체육공원1호 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
coat1()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
coat1()

print("-----------------------")

print("체육공원2호 체육시설")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
coat2()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
coat2()

print("-----------------------")

print("가운동 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
gown()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
gown()

print("-----------------------")

print("가운푸른물센터 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
puleun()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
puleun()

print("-----------------------")

print("별내택지지구체육공원")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
gigu()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
gigu()

print("-----------------------")

print("별내면 광전리 테니스장")
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[1]/a").click()
gwang()
browser.find_element_by_xpath("//*[@id='contents']/div[2]/ul[3]/li[2]/ul/li/ul/li[3]/ul/li[3]/a").click()
print("다음달")
gwang()

curs.execute("""DELETE FROM rese WHERE id IN
                (
                SELECT id FROM (SELECT id FROM rese GROUP BY rese_name, rese_date HAVING count(*) > 1 
                ) temp_table)""") #중복제거

curs.execute("""INSERT IGNORE reservation 
                SELECT * FROM rese
                WHERE id > 0 ORDER BY rese_name, rese_date; """) #정렬

rows = curs.fetchall()
for row in rows:
    print(row['id'], row['rese_name'], row['rese_date'])
conn.commit() 
conn.close()
browser.quit()