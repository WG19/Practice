from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
from datetime import datetime
def OrderedSet(list): #리스트 순서 유지하여 중복 제거
    my_set = set()
    res = []
    for e in list:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res
전체야구일정 = [[]]
chromdriver = r'C:\Users\earth\Downloads\chromedriver'
driver = webdriver.Chrome(executable_path=r"C:\Users\earth\Downloads\chromedriver\ChromeDriver.exe")
driver.implicitly_wait(1)
for year in range(2019, 2014, -1):
    경기일정 = []
    경기시간 = []
    경기취소 = []
    if year == 2019:
        endMonth = 9
    else:
        endMonth = 12
    for month in range(3, endMonth, 1):
        driver.get('https://sports.news.naver.com/kbaseball/schedule/index.nhn?date='+str(datetime.today().strftime("%Y%m%d"))+'&month='+str(month)+'&year='+str(year)+'&teamCode=')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        대분류 = soup.find_all('table', attrs={'cellspacing':'0'})
        for i in range(len(대분류)):
            중분류 = 대분류[i].find_all('td', {'rowspan':"5"})
            시간중분류 = 대분류[i].find_all('span', class_=['td_hour'])
            취소경기 = 대분류[i].find_all('span', class_=['suspended'])
            for k in range(len(중분류)):
                경기일정.append(str(year)+"."+중분류[k].select('span > strong')[0].get_text().strip())
                경기일정 = OrderedSet(경기일정)
                print(경기일정)
                print("/")
                if len(시간중분류) > 1:
                    print("1보다 큼")
                    print("취소경기 수 : " + str(len(취소경기)))
                    순환 = 5 - len(취소경기)
                    for z in range(1, 순환 + 1, 1):
                        print(z)
                        경기시간.append(시간중분류[0].get_text().strip())
                        경기일정.insert(z+2, str(시간중분류[0].text.strip()))
                #경기일정.insert(0, str(year))
                #경기일정.insert(2, 경기시간)
                print(경기일정)
                전체야구일정.insert(0, 경기일정)
                경기일정 = []
                경기시간 = []
전체야구일정 = DataFrame(전체야구일정).set_index([0, 1]).fillna('-')
전체야구일정.to_csv("baseball.csv", mode='w')

