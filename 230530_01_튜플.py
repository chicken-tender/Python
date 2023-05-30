# 튜플 : immutable, read only
# 변경할 수 없는 시퀀스 자료형, ()소괄호를 사용하여 생성 ([]대괄호는 리스트, {}중괄호는 딕셔너리)
person = ('홍길동', 22, '서울', True) # ❗️소괄호 생략 가능
'''
person[0] = '학생'
print(person) # TypeError!!
'''

# 리스트는 값 변경 가능(mutable)
person1 = ['홍길동', 22, '서울', True]
person1[0] = '학생' # print(person1) => ['학생', 22, '서울', True]

# 패킹, 언패킹 개념
# 튜플 언패킹(JavaScript의 구조 분해와 '유사'함)
nickname, age, address, isStudent = person
print(nickname) # 홍길동
print(age) # 22
print(address) # 서울
print(isStudent) # True

# 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = '이순신'
    age = 40
    city = '수원'
    return name, age, city
a, b, c = get_person()

# 기본적인 동작
tp = 1,2,3,4,3,2,1,3,3,6,4,3
print(tp.count(3)) # 원하는 데이터의 개수를 세어주는 함수 (리스트와 동일)
print(tp.index(1)) # 원하는 데이터의 시작 인덱스를 알려줌
print(len(tp)) # 튜플에 포함된 데이터의 개수
print(tp.__len__()) # len()과 동일

# 튜플에서는 삭제 안 됨