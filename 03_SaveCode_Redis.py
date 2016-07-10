# 生成200个序列码并存入Redis

import random
import string
import redis

# each code lenth
LENTH = 20
# code count
LIMIT = 200
# connect redis
DB = redis.Redis(host='localhost', port=6379, db=0)


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
    for i in range(len(code)):
        # insert
        DB.set(i, code[i])


# print codes
def main():
    code = [creatcode(LENTH) for i in range(LIMIT)]
    save(code)


if __name__ == '__main__':
    main()
    # print all keys and values
    for key in DB.keys('*'):
        val = DB.get(key)
        print(key, '=>', val)
