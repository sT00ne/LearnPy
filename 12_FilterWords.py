# 敏感词从files/filtered_words.txt获取,当用户输入敏感词时，用'*'隐去
import os
import sys


def confirmwords(word):
    filepath = os.path.abspath(os.path.join(sys.path[0], 'files', 'filtered_words.txt'))
    with open(filepath, 'r', encoding='UTF-8') as f:
        mylist = f.read().splitlines()
    for fword in mylist:
        if fword in word:
            word = word.replace(fword, '*')
    print(word)


if __name__ == '__main__':
    text = input('请输入:')
    confirmwords(text)
