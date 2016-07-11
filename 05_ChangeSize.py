# 对某路径下的图片重新设置大小
import os
import sys
from PIL import Image


def changesize(path, size):
    filetype = ('.jpg', '.png')
    for infile in os.listdir(path):
        # 后缀为图片格式
        if infile.endswith(filetype):
            outname = infile.split('.')
            try:
                im = Image.open(path + '/' + infile)
                print(im)
                outfile = im.resize(size)
                print(outfile)
                outfile.save(path + '/' + outname[0] + str(size) + '.jpg', "JPEG")
            except IOError:
                print("cannot create thumbnail for", infile)


def main():
    pwd = sys.path[0]
    filepath = os.path.abspath(os.path.join(pwd, 'imgs'))
    filesize = (125, 125)
    changesize(filepath, filesize)


if __name__ == '__main__':
    main()
