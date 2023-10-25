'''
문제
월 입력>> 12
일 입력>> 11
a.csv에 존재하는
12월 11일 최고 기온 데이터들과
최저 기온 데이터들을 한번에 show() 해주세요!
단, 범례를 maxTemp/minTemp로 해주시고
	빨간색/파란색 그래프로 표기해주세요!
'''
import matplotlib.pyplot as plt
import csv

MONTH=input('월 입력>> ')
DATE=input('일 입력>> ')

maxTempList=[]
minTempList=[]

with open('a.csv','r') as file:
    data=csv.reader(file)
    header=next(data)
    print(header)

    for row in data:
        if row[-1]=='' or row[-2]=='':
            continue
        if row[0].split('-')[1] == MONTH and row[0].split('-')[2] == DATE:
            maxTempList.append(float(row[-1]))
            minTempList.append(float(row[-2]))



plt.title('MONTH '+MONTH+'  DATE '+DATE)
plt.plot(maxTempList, color='red', label='maxTemp')
plt.plot(minTempList, color='blue', label='minTemp')
plt.legend()
plt.show()
