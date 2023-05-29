# 키와 값이 존재하는 자료 구조(자바의 Map과 유사) {}
# 키와 값의 구분은 ':' 입니다.
coffee_menu = {"Americano" : 2500, "Esspresso" : 2300, "Latte" : 3000}
tea_menu = {"MilkTea" : 4000, "BlackTea" : 3500, "GreenTea" : 3500}
food_menu = {"Cake" : 6800}

# 1. key로 value 확인하기
print(coffee_menu["Americano"])
# 2. get 함수로 value 확인하기
print(coffee_menu.get("Americano"))

# value 추가 및 삭제, key 존재 여부 확인
# 추가 : 딕셔너리[key] = value
# 삭제 : del 딕셔너리[key] (key로 value 삭제)
# key 존재 여부 확인 : if key in 딕셔너리
# 키로 값 확인 : 딕셔너리[key] 또는 딕셔너리.get(key)
# update 함수 : 딕셔너리의 데이터를 한꺼번에 변경 할 때 사용
# keys() : 딕셔너리에서 key를 가져옴
# values() : 딕셔너리에서 value를 가져옴

dict1 = {"자바": 80, "리액트": 90, "파이썬": 88}
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print("리액트" in dict1) # True
print("자바스크립트" in dict1) # False

print(dict1["파이썬"]) # 88 (없는 key 넣으면 KeyError 발생)

# 반복문과 함께 사용하기
for key in coffee_menu : # 딕셔너리를 키값 기준으로 자동 순회
    print(key, ":", coffee_menu[key])

menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."] 
}

while True :
    print("메뉴를 선택 하세요.")
    menu = input("[1] 보기 [2] 조회 [3] 추가 [4] 삭제 [5] 종료 : ")
    if menu == "1" :
        for key in menu_dic :
            print(key, ":", menu_dic[key])
    elif menu == "2" :
        select_name = input("조회할 메뉴명을 입력하세요. : ")
        if select_name in menu_dic :
            print(menu_dic[select_name])
        else :
            print("해당 메뉴는 존재하지 않습니다.")
    elif menu == "3" :
        add_name = input("추가 할 메뉴를 입력 하세요. : ")
        if add_name not in menu_dic :
            group = input("카테고리 : ")
            price = int(input("가격 : "))
            desc = input("설명 : ")
            menu_dic[add_name] = [group, price, desc] # 새로운 key로 value 추가
        else :
            print("해당 메뉴는 이미 존재합니다.")
    elif menu == "4" :
        del_name = input("삭제 할 메뉴를 입력 하세요. : ")
        if del_name in menu_dic :
            del menu_dic[del_name]
        else :
            print("해당 메뉴는 없습니다.")
    elif menu == "5" :
        print("영업을 종료 합니다.")
        break
    else :
        print("잘못 입력하셨습니다.")