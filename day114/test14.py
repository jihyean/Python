# 막대 그래프
# 히스토그램
# 자료의 분포(or 빈도) 상태를 막대 그래프로 표기한 것

import matplotlib.pyplot as plt
import random

##aList=[1,2,3,3,5]
##plt.hist(aList)
##plt.show()

# 주사위는 과연 공정할까?
dice=[] # 주사위를 굴리는 행위(==시행)의 결과를 저장할 리스트
for i in range(10000):
    dice.append( random.randint(1,6) ) # 1~6
##print(dice)
plt.hist(dice,bins=6) # 가로축 구간 설정 속성
plt.show()
