import matplotlib.pyplot as plt
import csv

maxTempList=[]

with open('a.csv','r') as file:
    data=csv.reader(file)
    header=next(data)
    print(header)

    for row in data:
        if row[-1]=='':
            continue
        if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '26':
            maxTempList.append(float(row[-1]))
        
print(len(maxTempList))



plt.title('maxTempList')
plt.plot(maxTempList, color='red', label='maxTempList')
plt.legend()
plt.show()
