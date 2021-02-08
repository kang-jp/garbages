import csv
import requests
from bs4 import BeautifulSoup
html=requests.get("https://hypixel-skyblock.fandom.com/wiki/Minions")
soup=BeautifulSoup(html.content,"html.parser")
table=soup.find_all("div",id="minProfTblCalcResult")[0]
# print(table.contents)
table=table.contents[0]
rows=table.findAll("tr")
tbl=[]
for row in rows:
    Row = []
    for cell in row.findAll(['td', 'th']):
        Row.append(cell.get_text())
    tbl.append(Row)

tbl=[tbl[i] for i in range(1,len(tbl))]
for i in range(len(tbl)):
    for j in range(len(tbl[i])):
        tbl[i][j]=tbl[i][j].replace('\xa0coins','')
        tbl[i][j]=tbl[i][j].replace(',','')
        tbl[i][j]=tbl[i][j].replace('ⓘ','')

tbl.sort(key=lambda x: -int(x[1]))
print(tbl)
import datetime

with open('sb.csv','a',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow([datetime.date.today()])
    writer.writerows(tbl)