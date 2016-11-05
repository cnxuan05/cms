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
    # s1 = 'Joey Huang'
    # m = re.match(r'(\w+) (\w+)', s1)
    # print(m.group(1))
    # print(m.groups())

    # greedy/non-greedy
    s = '<H1>title</H1>'
    print(re.match(r'<(.+?)>', s).group())


def re_pattern_syntax():
    
    pass

    # greedy/non-greedy
    # print(re.match(r'ab{2,4}?','abbbbbbbbbc').group())
    # []集合 16进制的值提取出来
    # print(re.search(r'\\','The \\ price is $9.00').group())
    # print(re.search(r'0[xX]([0-9A-Fa-f]{6})', 'The hex value is 0xFFF0263F8').groups())
    # print(re.search(r'(\d)(\d)(\d)\1\2\3','135 135').groups())
    # \d \D
    # print(re.search(r'\b(\d{3}-\d{4}-\d{4})\b','0dx0x 131-1324-5896').groups())
    # .IGNORECASE
    # print(re.match(r'(\w+)\s*'))

if __name__ == '__main__':
    re_pattern_syntax()
