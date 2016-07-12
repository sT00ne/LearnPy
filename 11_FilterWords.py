# 敏感词从files/filtered_words.txt获取，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
import os
import sys


def confirmwords(word):
    filepath = os.path.abspath(os.path.join(sys.path[0], 'files', 'filtered_words.txt'))
    with open(filepath, 'r', encoding='UTF-8') as f:
        mylist = f.read().splitlines()
    if word in mylist:
        print("Freedom")
    else:
        print("Human Rights")


if __name__ == '__main__':
    text = input('请输入:')
    confirmwords(text)
