import pandas as pd

# 2차원 배열 데이터가 존재하는 상황
# dict
data={ 'Name':['Alice','Bob','David'],
       'Score':[30,88,59],
        'City':['Chicago','New York','Los Angeles'] }
df=pd.DataFrame(data)
print(df)
print()
print()
print()
print(df['Name']) # 특정 열을 출력
print(df.loc[0]) # 특정 행을 출력
print(df[ df['Score']>=50 ]) # 조건만족하는 데이터만 추출

df['Age']=[20,22,21]
print(df)

ndata={'Name':'Anna','Score':85,'City':'Seoul','Age':30}
df=df._append(ndata,ignore_index=True)
# 인덱스를 재설정해서 새로운 행이 최신 행으로 추가될수있음
print(df)










