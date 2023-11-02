##import csv
##import matplotlib.pyplot as plt
##
##with open('apple.csv','r') as file:
##    data=csv.reader(file)
##    header=next(data)
##    print(header)
##    print()
##
##    sample=[]
##    area=input('출력할 지역 입력>> ')
##    for row in data:
##        if area in row[0]:
##            for v in row[3:]:
##                sample.append(int( v )) # v.replace(',','')
##print(sample)
##
##plt.plot(sample)
##plt.show()



import csv
import matplotlib.pyplot as plt
import numpy as np

with open('apple.csv','r') as file:
    data=csv.reader(file)
    header=next(data)
    print(header)
    print()

    area=input('출력할 지역 입력>> ')
    for row in data:
        if area in row[0]:
            sample=np.array(row[3:], dtype=int)
print(sample)

plt.plot(sample)
plt.show()
