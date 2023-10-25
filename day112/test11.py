# 데이터 시각화
'''
matplotlib 라이브러리
    pyplot 모듈
외부모듈을 설치 == pip
cmd >> pip install matplotlib
pip NOT FOUND == PATH 설정
'''
import matplotlib.pyplot as plt

aList=[10,20,30,40]
bList=[20,40,10,30]

plt.title('only ENGLISH') # 캡션 추가하기
plt.plot(aList, color='hotpink', label='aList') # 그래프 색 변경하기
plt.plot(bList, ls='--', label='bList') # 그래프 선 모양 변경하기
plt.legend() # label, 범례 추가하기
plt.show()
