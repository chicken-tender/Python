# 산술연산자 : +, -, *, /, %, //(몫), **(제곱 연산자)
i, j = 10, 3
print("%d + %d = %d"%(i,j, i+j))
print("%d - %d = %d"%(i,j, i-j))
print("%d * %d = %d"%(i,j, i*j))
print("%d / %d = %.2f"%(i,j, i/j))
print(i / j)
print(i // j)
print(i ** j)

# tax_rate = 0.10
# income = int(input("당신의 수입을 입력 하세요. : "))
# print(f"당신이 납부해야 할 세금은 {income * tax_rate} 입니다.")

# month_pay = float(input("당신의 월 실수령 : "))
# print(f"당신의 연봉은 {month_pay * 12 * 1.15:.2f}원 입니다.")

# 관계 연산자 (and, or, not), 대부분의 경우 비교연산자와 함께 사용되며, 참과 거짓을 판별 합니다.
# and : 둘 다 참이면 참
# or : 둘 중 하나만 참이면 참
# not : 현재 결과 부정
x, y, z = 10, 20, 30
rst1 = (x > 0) and (x > y) # False
rst2 = (x > 0) or (x > y) # True
rst3 = not((x > 0) or (x > y)) # False

print(rst1, rst2, rst3)

# 나머지 연산자와 다항연산자
# (조건) ? 참 : 거짓 => (조건) and 참 or 거짓
num = int(input("정수값을 입력 : "))
flag = (num % 2 == 0) and "짝수" or "홀수"
print(f"입력하신 숫자는 {flag} 입니다.")

age = 23
is_adult = (age >= 20) and "성인" or "미성년자"
print(is_adult)