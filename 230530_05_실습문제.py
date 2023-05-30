'''
문제 : 입력 받은 수가 소수인지 아닌지 판별하기 (함수 이용)
* 소수란? 1과 자기 자신 외에 나누어지지 않는 수
'''
# 숫자 입력 받기
# 소수 판별
# 출력

def is_prime(num) :
    for i in range(2, n) : # 1과 자기 자신 제외
        if num % i == 0 : return False
    return True
n = int(input("정수 입력 : "))

if(is_prime(n)) : print("소수")
else : print("소수 아님")