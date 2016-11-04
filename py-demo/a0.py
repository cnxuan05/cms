# coding:utf-8
import re


def re_demo():
    txt = 'If you purchase more than 100 sets, the price of product A is $9.90.'
    m = re.search(r'(\d+).*\$(\d+\.?\d*)', txt)

    print(m.groups())


def re_method():
    s = 'lazy fox jumps over lamp'
    print(re.search(r'^.*c', s))
    print(re.match(r'.*c', s))
    print(re.split(r'\W', s))

    s1 = 'Hello,this is Joey'
    s2 = 'The first price is $9.90 and the second price is $100.0'
    i = re.finditer(r'\d+\.?\d*', s2)
    for m in i:
        print(m.group())

    # print(re.sub(r'\d+\.?\d*', '<number>', s2))
    # print(re.subn(r'\d+\.?\d*', '<number>', s2))

def re_match_object():
    s1 = 'Joey Huang'
    m = re.match(r'(\w+) (\w+)', s1)
    print(m.group(1))
    print(m.groups())
if __name__ == '__main__':
    re_match_object()
