# coding:utf-8

'''
redis
'''
import redis
r = redis.Redis(host='localhost',port=6379,db=0)
r.set('foo','bar')
b = r.get('mynum')
r.delete('foo')
r.save()

p = r.pipeline(transaction=False)
p.set('hello','redis').sadd('faz','baz').incr('num').execute()
# pipe = r.pipeline(transaction=False)