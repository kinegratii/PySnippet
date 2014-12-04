#coding=utf8
import json
from obj2json import obj2dict

class A(object):

    def __init__(self, name, b):
        self.name = name
        self.b = b

class B(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

b1 = B(2,6)
print json.dumps(b1, default=obj2dict)

b_list = (B(1,3),B(2,5))
print json.dumps(b_list, default=obj2dict)
#  [{"y": 3, "x": 1}, {"y": 5, "x": 2}]

a = A('bob', b1)
print json.dumps(a, default=obj2dict)

b1 = B(b1,b1)
print json.dumps(b1, default=obj2dict)
