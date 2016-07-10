# 统计英文文档中的单词出现次数


import re


def getcount(path):
    with open(path, 'r', encoding="ISO-8859-1") as file:
        data = file.read(10000)
        # 只查找单词或者字母或者数字,不能查找到it's等有分隔符的单词
        words = re.compile('[a-zA-Z0-9]+')
        dict = {}
        i = 0
        for x in words.findall(data.lower()):
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
            i += 1
        for (k, v) in sorted(dict.items(), key=lambda x: x[1], reverse=True):
            print("dict[%s]=" % k, v)
        print('总单词数为:', i)


def main():
    getcount('files/Harry.txt')


if __name__ == '__main__':
    main()
