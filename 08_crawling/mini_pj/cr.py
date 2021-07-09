from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

def idk():
    if platform.system() == 'Windows':
        path = 'c:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname = path).get_name()
        rc('font', family = font_name)
    elif platform.system() == 'Darwin':
        rc('font', family = 'AppleGothic')
    else:
        print('Check your OS system')

    driver = webdriver.Chrome("/Users/Van/202105_lab/driver/chromedriver")
    url = "http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys=1982&ye=2021&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR&o2=OutCount&de=1&lr=5&tr=&cv=&ml=1&sn=30&si=&cn="
    driver.get(url)
    html = driver.page_source
    bsObject = BeautifulSoup(html, 'html.parser')

    temp = bsObject.find_all("table")[1]

    column = ["순","이름","팀","WAR","출장","완투","완봉","선발","승","패","세","홀드","이닝","실점","자책","타자","안타","홈런","볼넷","고4","사구","삼진","보크","폭투","ERA","FIP","WHIP","ERA+","FIP+","WAR"]
    df = pd.DataFrame(columns=column)
    templen = len(temp.find_all("tr"))
    
    for i in range(2, templen):
        tempTr = temp.find_all("tr")[i]
        if(tempTr.find("th") is not None):
            continue
        row = {}
        column_idx = 0
        for j in range(len(column)):
            tempTd = tempTr.find_all("td")[j].text
            if(tempTd == "" and j > 0):
                continue
            row[column[column_idx]] = tempTd
            column_idx += 1
        df = df.append(row,ignore_index=True)

    # df_league = df[df['이름'] == "리그"].reset_index(drop=True)

    df_team = df[df['이름'] != "리그"].iloc[:,1:].reset_index(drop=True)
    # 공백제거
    df_team = df_team.apply(lambda x: x.str.strip())
    df_stat = df_team.iloc[:,:9]

    df_stat["팀"] = df_stat["팀"].astype(int)
    df_stat["WAR"] = df_stat["WAR"].astype(float)
    df_stat[["출장", "완투", "완봉", "선발", "승", "패"]] = df_stat[["출장", "완투", "완봉", "선발", "승", "패"]].astype(int)

    df_stat["tmp"] = np.where(df_stat.팀 < 50, 2000, 1900)
    df_stat["팀"] = df_stat["tmp"]+df_stat["팀"]
    df_stat = df_stat.iloc[:,:-1]

    df_stat_array = df_stat[df_stat["이름"]=="삼성"][["팀", "완투"]].to_numpy().tolist()
    df_stat_array.sort()

    return df_stat_array

