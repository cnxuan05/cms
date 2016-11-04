# coding:utf-8
import urllib
import urlparse
import datetime

gp_variable = '000001.sz'
gp_variable2 = '600000.ss'
sz_path = 'http://table.finance.yahoo.com/table.csv?s=' + gp_variable
ss_path = 'http://table.finance.yahoo.com/table.csv?s=' + gp_variable2

'''
a b c d e f s

'''
full_path = 'http://table.finance.yahoo.com/table.csv?' + 'a=0&b=1&c=2002&d=10&e=3&f=2016&s=' + gp_variable2
print full_path

print(sz_path)
print(ss_path)


def urlencode():
    params = {'score': 100, 'name': 'coding', 'comment': 'very good'}
    qs = urllib.urlencode(params)
    print(qs)
    pa = urlparse.parse_qs(qs)
    print(pa)


def parse_qs():
    url = 'https://www.google.com.hk/#newwindow=1&safe=strict&q=bekk-garch%E6%A8%A1%E5%9E%8B'
    result = urlparse.urlparse(url)
    print(result)
    pass


def download_stock_data(stock_list):
    for sid in stock_list:
        url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
        fname = sid + '.csv'
        print ('downloading %s from %s ' % (fname, url))
        urllib.urlretrieve(url, fname)
    pass


def download_stock_data_in_period(stock_list, start, end):
    for sid in stock_list:
        params = {'a': start.month - 1, 'b': start.day, 'c': start.year, 'd': end.month - 1, 'e': end.day,
                  'f': end.year, 's': sid}
        url = 'http://table.finance.yahoo.com/table.csv?'
        qs = urllib.urlencode(params)
        url = url + qs
        fname = '%s_%d%d%d_%d%d%d.csv' % (sid, start.year, start.month, start.day, end.year, end.month, end.day)
        print ('downloading %s from %s ' % (fname, url))
        urllib.urlretrieve(url, fname)
    pass


if __name__ == '__main__':
    stock_list = ['300001.sz', '300002.sz']
    # download_stock_data(stock_list)
    start = datetime.date(year=2002, month=1, day=1)
    end = datetime.date(year=2016, month=11, day=3)
    download_stock_data_in_period(stock_list, start, end)
    # parse_qs()

print 'end_of_file'
