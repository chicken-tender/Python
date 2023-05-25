# 조건문 : if ~ else
num = int(input("정수를 입력 하세요 : "))
if num % 2 == 0 :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")

# 조건문 : if ~ elif ~ else
n = int(input("정수 입력 : "))
if n > 100 :
    print("100 보다 커요.")
elif n < 100 :
    print("100 보다 작아요.")
else :
    print("100과 같아요.")

# 회원가입을 위한 아이디, 비밀번호 입력 받기
# string.find(찾을 문자)
# string.find(찾을 문자, 시작 index)
# string.find(찾을 문자, 시작 index, 끝 index)
user = input("아이디 : ")
if len(user) >= 10 :
    pw = input("비밀번호 입력 : ")
    if(pw.__len__() < 8 or pw.__len__() > 16) :
        print("비밀번호는 8자리 이상 16자리 이하여야 합니다.")
    else :
        print(f"아이디 : {user}, 비밀번호 : {pw}")
else :
    print("아이디는 반드시 10자리 이상이어야 합니다.")