import csv
import matplotlib.pyplot as plt
import numpy as np

pdatas = None       # 초기에 sample을 None으로 설정

count = 0           # 입력 값이 포함된 동 갯수 
while count != 1:   # 해당 이름을 가진 동이 하나인 경우가 아니라면(하나만 있을때까지)
    with open('korea.csv', 'r') as file:    # 'korea.csv' 파일을 읽기 모드로 열기
        data = csv.reader(file)             # CSV 파일을 읽기 위해 csv.reader 함수를 사용
        print()

        area = input('동 이름 입력>> ')     # 검색할 동 이름 입력받아 area 변수에 저장
        
        for row in data:                    # 데이터의 처음부터 끝까지 행 반복
            if area in row[0]:              # 해당 행의 첫번째 열(인덱스 0)에 area 변수 값이 포함 여부 검사
                print(row[0])               # 포함시 출력
                pdatas = np.array(row[3:], dtype=int)   # 해당 동의 정보 저장(4번째 열부터 끝까지)
                count = count + 1                       # 저장하였으므로 카운트 1증가

        if count == 0:                                  # 해당 이름을 가진 동이 없을시
            print('해당 이름을 가진 동은 없습니다!')
            print('다시 입력하세요!')

        elif count > 1:                                 # 해당 이름을 가진 동이 여러개일 경우
            count = 0                                   # 다시 반복해야 하기 때문에 count 초기화
            print('해당 이름을 가진 동이 여러개입니다!')
            print('정확하게 입력해주세요!')

if pdatas is not None:  # pdatas 값이 존재시
    plt.plot(pdatas)    # Matplotlib을 사용하여 sample 배열의 데이터를 그래프로 작성
    plt.show()          # 해당 그래프 화면에 출력
