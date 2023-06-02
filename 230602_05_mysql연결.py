import pymysql

# MySQL 연결하기
conn = pymysql.connect(host="127.0.0.1", user="root", password="", db="mysqlDB", charset="utf8")

# 커서 생성하기
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE userTable (id char(10), userName char(15), email char(20), birthYear int)")

# 데이터 입력 하기
cur.execute("INSERT INTO userTable VALUES('ayj', '안유진', 'ayj@gmail.com', 2003)")
cur.execute("INSERT INTO userTable VALUES('jwy', '장원영', 'jwy@gmail.com', 2004)")

# 데이터 저장하기
conn.commit()

# 연결 종료하기
conn.close()