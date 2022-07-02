# --*--coding: utf-8 --*--
"""
Created with IntelliJ PyCharm.
@Time: 2022/7/2 16:09
@PROJECT_NAME: chhTricks
@File: replace_markdown_equation
@Author: chh3213
@Email:
@Description:
"""

import re
PATH = '<img src="https://www.zhihu.com/equation?tex={}" alt="{}" class="ee_img tr_noresize" eeimg="1">'


def replace_markdown_equation(source_file:str, target_file:str, enable_tag=True):
    if not (source_file.endswith(".txt") or source_file.endswith(".md")):
        return False, "文件格式问题，仅仅支持txt或md"

    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()

    line_equations_format = re.compile(r'\$\$(.*?)\$\$', re.S)  #最小匹配
    line_equations = re.findall(line_equations_format, content)
    for index, line_equation in enumerate(line_equations):
        tag = "\\tag{" + str(index+1) + "}" if enable_tag and "\\tag" not in line_equation else ""
        prev_eq = "$${}$$".format(line_equation)
        new_eq = "\n{}\n".format(PATH.format(line_equation+tag, line_equation+tag))
        content = content.replace(prev_eq, new_eq)

    inline_equations_format = re.compile(r'\$(.*?)\$', re.S)  # 最小匹配
    inline_equations = re.findall(inline_equations_format, content)
    for index, inline_equation in enumerate(inline_equations):
        prev_eq = "${}$".format(inline_equation)
        new_eq = "\n{}\n".format(PATH.format(inline_equation, inline_equation))
        content = content.replace(prev_eq, new_eq)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    s = "E:\CHH3213_KING\hexo_blog\source\_posts\【自动驾驶】决策规划面试准备（持续更新）.md" # 修改前的文件路径
    t = "E:\CHH3213_KING\hexo_blog\source\_posts\ after_convert.md"  # 修改后的文件路径
    replace_markdown_equation(s, t, True)