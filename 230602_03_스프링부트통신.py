import requests
import json

data = {
    "id" : "홍길동",
    "pwd" : "d#dkfjTdf10"
}

# JSON 데이터를 서버로 전달
url = "http://localhost:8111/login"
header = {"Content-Type" : "application/json"}

response = requests.post(url, data=json.dumps(data), headers=header)

if response.status_code == 200 :
    print("데이터 전송 성공")
else : print("데이터 전송 실패")