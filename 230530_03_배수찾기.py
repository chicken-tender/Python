# 배수 찾기
# 문제 : 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램 작성
# 입력 : 첫째 줄에 n이 주어진다. 다음 줄 부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다. 이 수는 0 보다 크고, 10,000보다 작다.
# 목록은 0으로 끝난다.
# 출력 : 목록에 있는 수가 n의 배수인지 아닌지 구한 뒤 예제 출력처럼 출력하시오.
'''
예제)
3
1
7
99
321
777
0

출력)
1 is NOT a multible of 3.
7 is NOT a multiple of 3.
99 is a multiple of 3.
321 is a multiple of 3.
777 is a multiple of 3.
'''

list = []
n = int(input("배수 입력 : "))
while True :
    a = int(input("정수 입력 : "))
    if (a != 0) :
        list.append(a)
    else : break
for e in list :
    if(e % n == 0) : print(f"{e} is a multiple of {n}.")
    else : print(f"{e} is NOT a multiple of {n}.")