# coding:utf-8
import urllib


def print_list(list):
    for i in list:
        print(i)
    pass


def demo():
    pass
    # s = urllib.urlopen('http://www.baidu.com')
    # msg = (s.info())
    # print_list(dir(msg))
    # print_list(msg.headers)
    # print(msg.getheader('Content-Type'))


def retrieve():
    urllib.urlretrieve('http://www.sina.com', 'index.html', reporthook=progress)


def progress(blk, blk_size, total_szie):
    print('%d/%d - %.02f%%' % (blk * blk_size, total_szie, (float)(blk * blk_size) * 100 / total_szie))
    pass


if __name__ == '__main__':
    retrieve()
    pass
'''
200:
206:
301:重定向
302:
303:
400:bad request
404:not found
500:服务端错误

一部分 应答的头部
第二部分 主体的内容

URL参数规则--&a=1&b=2&c=3&
domian and path
expires
http-only

登陆信息--判断用户是否已经登陆
购物车--保存用户购买的商品列表

cookie 可能引起什么样的安全问题


'''
