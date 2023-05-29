# 연속적으로 데이터를 저장하는 자료형, 동적으로 크기가 변경 됨. 다른 타입 데이터를 함께 사용 가능 (다른 배열, ...)
# 읽고 쓰기가 가능한 mutable []

numbers = [1,2,3,4,5]
fruits = ['apple', 'banana', 'cherry', 'lemnon']
mixed = [1, 'symbol', True, 3.14, [1,2,3]]
empty = []

# 변수 사용 대비 이점
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# total = kor + eng + mat
# print(f"평균 : {total / 3}")

# score = list(map(int, input("성적 입력 : ").split()))
# print(f"평균 : {sum(score) / len(score)}")
print(mixed[1:3])

s = ["korea", "seoul", "incheon", [1,2,3,4,5], ["안유진", "카리나", "민지"]]
print(s[0][1])
print(s[3][4])

# 리스트 연산자 : 연결(+), 반복(*)
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a*3)
print(list_a + list_b)

# 리스트 요소 추가
# append : 리스트의 끝에 값 추가
# insert : 특정 위치에 값 추가
list_c = [1,2,3]
list_c.append(4)
list_c.append(10)
list_c.insert(1, 22)
print(list_c)

# 리스트 제거 하기
# pop : 인덱스가 없으면 마지막 요소 반환하고 삭제, 인덱스가 있으면 인덱스의 위치의 데이터 삭제, 인덱스 범위를 벗어나면 error 출력
# reemove : 값으로 제거, 동일한 값이 여러개 있는 경우에는 낮은 인덱스 부터 제거
# clear : 모든 값을 지우고 빈 리스트만 남김
# del 리스트명[인덱스] : 해당 값 제거
list_all = [0,1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd', 'e', 'f', 'ko']
list_all.pop() # 인덱스가 없으므로 마지막 요소 제거
list_all.pop(8) # 해당 인덱스 값 제거
list_all.insert(8,8)
del list_all[0]
# print(list_all)

# 중복 제거
my_list = ["A", "B", "C", "D", "A", "B", "E", "F"]
new_list = []
for e in my_list : # my_list 리스트를 요소값 기준으로 자동 순회
    if e not in new_list :
        new_list.append(e) # 리스트의 끝에 값을 추가하는 함수
print(new_list)

# 정렬
arr = [1,4,5,66,777,1000,234,456,56,75]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

# 리스트의 모든 요소 탐색하기
name_x = ["안유진", "장원영", "가을", "이서", "리즈"]

for e in name_x :
    print(e)

for i in range(len(name_x)) :
    print(name_x[i])

# 응용 문제 : 홀수, 짝수 나누어 담기
# 기본 코드
num = list(map(int,input("숫자를 입력하세요. : ").split()))
even = [] # 짝수 저장
odd = [] # 홀수 저장
for e in num :
    if(e % 2 == 0) : even.append(e)
    else : odd.append(e)
print(f"짝수 : {even}")
print(f"홀수 : {odd}")

# 람다 코드
number = list(map(int, input("숫자를 입력하세요. : ").split()))
even = list(filter(lambda x: x % 2 == 0, number)) # number의 요소값은 x
odd = list(filter(lambda x : x % 2 != 0, number))
print(f"짝수 : {even}")
print(f"홀수 : {odd}")
