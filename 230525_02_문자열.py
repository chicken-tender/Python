# 여러줄로 이루어진 문자열은 따옴표 3개 사용(""" """, ''' ''')
print("""동해물과 백두산이
마르고 닳도록 하느님이 보우하사
우리나라 만세 ...""")

print("저의 \"이름\"은 '홍길동' 입니다.")

# 이스케이프 문자 사용
print("서울시\t강남구\t역삼동")
print("사과\r바나나\r오렌지")

# 인덱싱 (슬라이싱) : 인덱스는 항상 0에서 부터 시작 합니다.
jumin = "991120-1234567"
print("성별 : " + jumin[7]) # 1은 남성
print("태어난 연도 : " + jumin[:2]) # 시작 인덱스를 주지 않으면 0에서 시작하고 end는 미만 개념
print("월 : " + jumin[2:4]) # 2번 인덱스 부터 4 미만
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리(1) : " + jumin[7:])
print("뒤 7자리(2) : " + jumin[-7:])

print("안녕하세요"[:2]) # 안녕
print("안녕하세요"[-3:]) # 하세요

a = "Life is too short, You need Python."
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "K" 문자열 요소는 변경할 수 없음

# 대소문자 바꾸기
a = "Hello Python Program..."
print(a.upper())
print(a.lower())

# 문자열 변경하기 : replace("","")
input_str = "Python Program"
new_str = input_str.replace("Python", "React")
print(new_str)

# 문자열에 포함된 문자 갯수 세기 및 문자열 길이
# 갯수 세기 : count()
# 길이 반환 : __len__(), len()
print(input_str.count("P"))
print(input_str.__len__()) # 문자열에 포함된 내장 함수
print(len(input_str)) # 외부 len() 함수

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 첫번째 인덱스 반환, 문자열을 찾지 못하면 -1을 반환
# rfind() : reverse의 의미로 뒤에서 부터 해당 문자열을 찾지만 인덱스는 앞에서부터 계산
# index() : 찾은 문자열의 첫번째 인덱스 반환, 문자열을 찾지 못하면 valueError 예외 발생

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장")) # 0
print(phrase.rfind("가장")) # 34
print(phrase.index("가장")) # 0
# 없는 문자열 찾기
print(phrase.find("나에게")) # -1
# print(phrase.index("나에게")) # ❗️valueError

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 연산자
# "문자열" + "문자열"
# "문자열" * (정수값) : 뒤에 오는 숫자 만큼 문자열을 반복
print("태양고 " * 2)
print("안녕하세요", "!"*5)

# 문자열의 양 옆 공백 제거 : strip()