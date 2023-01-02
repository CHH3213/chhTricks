import numpy as np 
import string

# 去除相关介词的大写
e_list = ['of', 'the', 'for', 'with', 'and', 'in', 'to', 'on', 'at']


def new_str(x):
    """将字符串中的单词（除去预先给定的单词列表）首字母大写

    Args:
        x (_type_): 预处理字符串

    Returns:
        _type_: 除给定单词之外单词首字母大写后的字符串
    """
    return ' '.join([a.title() if (not a in e_list and not a.isupper()) else a for a in x.split()])


if __name__=='__main__':
    f = open('bib.bib', 'r', encoding='UTF-8')  # 读取想要修改的bib参考文献
    fw = open('bib_update.bib', 'w')  # 写入新的bib文件中
    lines = f.readlines()
    for line in lines:
        # if(line[2:7]=="title"):
        if("title" in line[0:10] and "booktitle" not in line[0:10]):
            new_line = line.replace('{', '{{')
            new_line = new_line.replace('}', '}}')
            # print(new_line[0:9])
            # final_line = new_line[0:9] + string.capwords(new_line[9:])+'\n'
            # final_line = new_line[0:9] + new_line[9:].title()
            final_line = new_line[0:9] + new_str(new_line[9:])+'\n'
            fw.write(final_line)
            print(final_line)
        else:
            fw.write(line)
    fw.close()
