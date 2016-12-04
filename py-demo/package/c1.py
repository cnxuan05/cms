# coding: utf-8


def demo():
    pass
    return '123'


def foo(name='', action="去砍柴", where="北京"):
    print name, where, action
    yield 1

    yield 12
    yield 13
    yield 14
    yield 15


def login(username):
    if username == 'alex':
        pass
        print '登录成功·'
    else:
        print '登录失败'


def show(**kargs):
    for item in kargs.items():
        print(item)


def my_orm():
    import MySQLdb
    return ''


# 简单的生成器 延迟生成
def p1():
    seek = 0
    while True:
        with open("d:/d.txt", 'r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return


def p2():
    result = 'gt' if 1 > 3 else 'lt'
    # python 保留的关键字
    temp = lambda x, y: x + y
    # $print(temp(4, 10))
    # temp2 = map(lambda x:x**x,range(10))# [x**2 for x in range(10)]
    # print(temp2)

    return ''


def foo2(arg):
    return arg + 100


def foo3(arg):
    if arg < 22:
        return True
    else:
        return False


def p3():
    li = [11, 22, 33, 44, 55, 66]
    # temp = map(foo2,li) # map(lambda arg: arg + 100, li)
    # temp = filter(foo3, li)    # 定义了新的过滤条件

    # print(reduce(lambda x, y: x * y, li))
    # print(temp)

    x = [1, 2, 3]
    y = [1, 2, 3]
    z = [1, 2, 3]
    q = [1, 2, 1]
    # print(zip(x, y, z, q))
    print(eval('8*8'))


#


def my_md5():
    # import md5
    import hashlib
    hash = hashlib.md5()
    hash.update('admin97986527')
    # print hash.digest()
    print hash.hexdigest()
    pass


def p6():
    # 把列表序列化为字符串的形式 默认是人不可读的 肉眼可以看出格式
    import pickle
    li = {'k1': '123', 'k2': '456'}  # 列表本质上也是一种对象

    # 把字符串写进了文件
    # dumpsed = pickle.dumps(li)
    # pickle.dump(li,open('d:/e.txt','w'))
    result = pickle.load(open('d:/e.txt', 'r'))
    # print result

    # 文件和 文件之间共享为什么需要 序列化-- >实现了2个python内存数据的交互

    # print type(p_str)
    # s_str = pickle.loads(p_str)
    # print type(s_str)

    # 字典 列表 集合 常规的数据格式的序列化
    import json
    name_dic = {'name': 'wupeiqi', 'age': 23}
    serialized = json.dumps(name_dic)
    name_data = json.loads(serialized)
    print name_data


def p7():
    # re.match(pattern,string) 从起始的位置匹配 1非贪婪模式
    # re.search 整个字符串匹配
    import re
    # s_str = re.match('\d+','aefasdf21342asfdf234234')
    # s_str = re.findall('\d+', 'aefasdf21342asfdf234234')
    # if s_str:
    #     print s_str[0]
    # s_str2 = re.search('\d+', '123aefasdf21342asfdf234234')

    # 编译之后生成了一个对象
    re_str2 = re.compile('\d+')
    # print s_str2.group()
    # print (re_str2.findall('123aefasdf21342asfdf234234'))
    s_str3 = re.search('(\d+)\w*(\d+)', 'as  2341asdfa1243123')
    print s_str3.group()
    print s_str3.groups()


def login():
    pass


def logout():
    pass


def p8():
    # 在浏览器上
    raw_data = raw_input('请输入地址: ')
    ay_data = raw_data.split('/')

    # from backend import account
    # import backend.account
    # @account.login()
    #  if raw_data == 'account/login':
    #      account.login()
    #  elif raw_data == 'account/logout':
    #      account.logout()
    #
    userspance = __import__('backend.' + ay_data[0])
    model = getattr(userspance, ay_data[0])
    func = getattr(model, ay_data[1])
    func()

    # from  backend import account
    # import backend.account
    # backend.account.login()
    # backend.account.logout()
    # pass

def p91(fun):
    def wrapper():
        print '调用装饰器'
        fun()
        print '嘎嘎嘎 '
    return wrapper
    pass

@p91
def p9():

    print '123'
    pass


































































































































































