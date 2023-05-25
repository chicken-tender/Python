# 한번에 변수에 값 할당하기
a = b = c = 1
print(a,b,c)

a,b,c = 1, True, "곰돌이"
print(a,b,c)

# 변수의 타입 확인
age = 100
is_adult = True
gender = "Male"
score = 95.34
print(type(age)) # int
print(type(is_adult)) # bool
print(type(gender)) # str
print(type(score)) # float

# 형변환 : 선언된 변수에 값이 할당되는 순간에 형이 결정되고 이후 다른 데이터형으로 변경하는 것을 의미함
print(str(10)+"10")
print(10+int("10"))

x,y,z = -1, 10, "test"
print(bool(x)) # True (0을 제외한 정수값은 True)
print(bool(y)) # True
print(bool(z)) # True
print(bool("")) # False
print(bool(0)) # False
print(bool(None)) # False