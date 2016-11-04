# coding:utf-8
import requests


def get_json():
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)
    print(r.json())


def get_querystring():
    url = 'https://httpbin.org/get'
    params = {'qs1': 'value1', 'qs2': 'value2'}
    r = requests.get(url, params=params)
    print(r.status_code)
    print(r.content)


def get_custom_headers():
    url = 'https://httpbin.org/get'
    headers = {'x-header1': 'value1', 'x-header2': 'value2'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.content)
    pass


def get_cookie():
    headers = {'User-Agent': 'Chrome'}
    url = 'http://www.douban.com'
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.cookies['bid'])


if __name__ == '__main__':
    get_cookie()
'''
http://docs.python-requests.org/en/master/


'''