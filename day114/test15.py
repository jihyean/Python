# 문제
# a.csv에 기온 데이터가 저장되어있습니다.
# 최저 기온의 분포도와 최고 기온의 분포도를 출력해주세요!~~

import csv
import matplotlib.pyplot as plt

maxTempList=[] # 8월 데이터
minTempList=[] # 1월 데이터

with open('a.csv','r') as file:
    data=csv.reader(file)
    header=next(data)
##print(header)
# 최고 기온 [-1]   최저 기온 [-2]

    for row in data:
        if row[-1]=='' or row[-2]=='':
            continue
        month=row[0].split('-')[1]
        if month=='08':
            maxTempList.append(float(row[-1]))
        elif month=='01':
            minTempList.append(float(row[-2]))

plt.hist(maxTempList,color='red',label='08')
plt.hist(minTempList,color='blue',label='01')
plt.legend()
plt.show()


        
