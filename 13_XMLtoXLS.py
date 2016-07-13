# 从xml转换到xls
# 使用xml.etree读取xml
# 使用xlwt保存至xls

import xml.etree.ElementTree as ET
import os
import sys
import xlwt


def transfer(filepath, xlspath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, 'name')
    ws.write(0, 1, 'rank')
    ws.write(0, 2, 'year')
    ws.write(0, 3, 'gdppc')
    i = 1
    for child in root:
        j = 0
        ws.write(i, j, child.attrib['name'])
        for grandchild in child:
            j += 1
            ws.write(i, j, grandchild.text)
        i += 1
    wb.save(xlspath)


if __name__ == '__main__':
    xml = os.path.abspath(os.path.join(sys.path[0], 'files', 'student.xml'))
    xls = os.path.abspath(os.path.join(sys.path[0], 'files', 'student.xls'))
    transfer(xml, xls)
