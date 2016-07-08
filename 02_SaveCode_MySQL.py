# 生成200个序列码并存入MySQL

import random
import string
import pymysql

# each code lenth
LENTH = 20
# code count
LIMIT = 200


# return a radom digit or letter
def radomcode():
    return random.choice((string.digits + string.ascii_letters))


# create a code
def creatcode(lenth):
    code = [radomcode() for i in range(lenth)]
    return "".join(code)


# save to mysql
def save(code):
    if len(code) == 0:
        pass
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8')
    cur = conn.cursor()
    for i in range(len(code)):
        cur.execute("INSERT INTO db_code (code) VALUES('"+code[i]+"')")
    cur.execute("SELECT * FROM db_code")
    print(cur.description)
    for row in cur:
        print(row)
    cur.close()
    conn.close()


# print codes
def main():
    code = [creatcode(LENTH) for i in range(LIMIT)]
    save(code)


if __name__ == '__main__':
    main()
