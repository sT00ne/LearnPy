# 简易验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
import os
import random
import string


def randomtext():
    return random.choice((string.digits + string.ascii_letters))


def randombgcolor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def randomtextcolor():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def creatimage(width, height, padding):
    pwd = sys.path[0]
    filepath = os.path.abspath(os.path.join(pwd, 'files'))
    # 新建白色为底色的图片
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    # 字体及字号
    fnt = ImageFont.truetype(filepath + '/arial.ttf', 40)
    # 修改底色
    d = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            d.point((x, y), fill=randombgcolor())
    # 添加字母
    for i in range(padding, width - padding, int((width - padding) / 4)):
        print(i)
        d.text((i, padding), randomtext(), font=fnt, fill=randomtextcolor())
    # 模糊处理
    img = img.filter(ImageFilter.BLUR)
    img.save(filepath + "/CAPTCHA.png", "PNG")


if __name__ == '__main__':
    width = 200
    height = 100
    padding = 30
    creatimage(width, height, padding)
