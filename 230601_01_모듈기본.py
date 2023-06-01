'''
🌵 모듈 가져오는 법 3가지
(1) 전체 가져오기 : import math
(2) 필요한 것만 가져오기 : from math import sin, cos, tan, floor, ceil
(3) 별칭 : import math as m
'''
import sys # 시스템 관련 정보를 가지고 있는 모듈. 주로 매개변수를 받을 때 사용
import os
print("명령줄 인수 : ", sys.argv) # 명령줄 인수 출력

# 스크립트 실행 경로
print("실행 경로 : ", sys.path[0])

# 프로그램 종료
# sys.exit(0)

# 현재 작업 디렉토리 가져오기
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 파일 존재 여부 확인
is_file = os.path.isfile('파일명.py')
# print(is_file)

# 시스템 명령어 출력
os.system("ls -l")