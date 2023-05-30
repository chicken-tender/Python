# 집합은 주로 다른 자료형의 중복 제거할 때 자주 사용 합니다.
# 순서 없음, 중복 불가, mutable(읽기/쓰기 가능)

# 중복 제거
s1 = set([1,2,3,4,5,1,2,3,4,5,1,3,4,5])
print(s1) # {1, 2, 3, 4, 5}

# 교집합 : 양쪽에 모두 존재하는 요소만 선택
s2 = set([1,2,3,4,5])
s3 = set([1,4,6,7])
print(s2.intersection(s3)) # {1, 4}

# 합집합
print(s2.union(s3)) # {1, 2, 3, 4, 5, 6, 7}

# 차집합
print(s2.difference(s3)) # {2, 3, 5}

# 중복 제거로 로또 번호 만들기
import random
lotto = set()
while True :
    num = random.randrange(1,46)
    lotto.add(num)
    if len(lotto) == 6 : break

print(lotto)