# 기본문법
# csv 파일
# 라이브러리
# matplotlib(데이터 시각화), numpy(리스트!=배열, 배열을 다루는 라이브러리), pandas(데이터 프레임을 다루는 라이브러리)

# pandas
# 데이터 프레임 == 테이블 형태의 데이터 == 2차원 배열
#  : 행과 열
#  행 == 인덱스 index
#  열 == 컬럼 column

import pandas as pd
import numpy as np

index=pd.date_range('11/1/2023',periods=8)
# 11월 1일부터 8일까지 총 8개의 행(index)을 생성

df=pd.DataFrame(np.random.rand(8,3),index=index,columns=list('ABC'))
# numpy 라이브러리로 8행 3열짜리 랜덤 데이터 생성
# 행을 index로, 열을 'ABC'로 설정
print(df)
print()
print()
print()
print(df['C'])
print()
print()
print()

df2=df[df['A']<0.6]
print(df2)

print()
print()
print()
print(df['A']>=0.5)

df['D']=df['A']/df['B']
print(df)
df.to_csv('final.csv')



