import csv
import datetime

data=[]
with open('sb.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            data.append(row)

header=data[0]
data=data[1:]

fmt=[]
tmp={}
for row in data:
    if len(row)==1:
        if tmp!={}:
            fmt.append([index,tmp])
        # yy,mm,dd=map(int,row[0].split('-'))
        # index=datetime.date(yy,mm,dd)
        index=row[0]
        tmp={}
        
    else:
        tmp[row[0]]=int(row[-1])
fmt.append([index,tmp])
# print(fmt)
    
from matplotlib import pyplot as plt

N=len(fmt)
x=list(range(N))
xn=[fmt[i][0] for i in range(N)]
KEYSS=list(fmt[0][1].keys())



cmds=['show','white','exit']
while 1:
    print(*cmds)
    inp=input()
    if not (inp in cmds):
        print('invalid command')
    if inp=='exit':
        break
    if inp =='show':
        KEYS=[]
        for key in KEYSS:
            flag= max([fmt[i][1][key] for i in range(N)])>=5*10**4
            if flag:
                KEYS.append(key)
        KEYS.sort(key=lambda key: -max([fmt[i][1][key] for i in range(N)]))
        KEYS=KEYS[:min(10,len(KEYS))]

        # KEYS=KEYSS

        for key in KEYS:
            y=[fmt[i][1][key] for i in range(N)]
            plt.plot(x,y,label=key)
        plt.xticks(x,xn)
        plt.ylim(0,15*10**4)
        plt.legend()
        plt.show()
    
    if inp=='white':
        KEYS=['Iron','Jungle','Sheep','Melon','Lapis']

        # KEYS=KEYSS

        for key in KEYS:
            y=[fmt[i][1][key] for i in range(N)]
            plt.plot(x,y,label=key)
        plt.xticks(x,xn)
        plt.ylim(0,15*10**4)
        plt.legend()
        plt.show()