#coding=utf8
"""将对象转化为JSON格式，支持对象的属性又是另一个的嵌套情况
"""
import json

def obj2dict(obj):
    # 基本数据类型，直接返回
    if not hasattr(obj,'__dict__'):
        return obj
    res = {}
    for k,v in obj.__dict__.items():
        if k.startswith('-'):
            continue
        if isinstance(v,list):
            ele = [obj2dict(item) for item in v]
        else:
            ele = obj2dict(v)
        res[k] = ele
    return res

class NestedObjJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        return obj2dict(obj)


def main():
    class A(object):
        def __init__(self, name,age):
            self.name = name
            self.age = age

    class B(object):
        def __init__(self,name,stu):
            self.name = name
            self.stu = stu

    b = B('bob',A('fe',10))
    b1 = B('nincy', A('by',20))
    #Result:{"stu": {"age": 10, "name": "fe"}, "name": "bob"}
    print json.dumps(b,cls=NestedObjJsonEncoder)

    #[{"stu": {"age": 10, "name": "fe"}, "name": "bob"}, {"stu": {"age": 20, "name": "by"}, "name": "nincy"}]
    print json.dumps([b,b1], default=obj2dict)

if __name__ == '__main__':
    main()

