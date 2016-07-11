import os
import sys
import re


def Analysis(path, type):
    count = [0, 0, 0]
    for file in os.listdir(path):
        if file.endswith(type):
            # 按行读取文件
            f = open(file, 'r', encoding='UTF-8').readlines()
            for line in f:
                # 备注行
                if re.match(r'^\s*#', line):
                    count[2] += 1
                # 空行
                elif line == '\n':
                    count[1] += 1
                else:
                    count[0] += 1
    print("总计:")
    print("代码行数:", count[0])
    print("空行数:", count[1])
    print("备注行数:", count[2])


if __name__ == '__main__':
    filepath = os.path.abspath(os.path.join(sys.path[0]))
    filetype = '.py'
    Analysis(filepath, filetype)
