# 生成200个序列码

import random
import string

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


# print codes
def main():
    for i in range(LIMIT):
        print(creatcode(LENTH))


if __name__ == '__main__':
    main()
