# obj2json

将对象转化为JSON格式，支持对象的属性又是另一个的嵌套情况。

## 开始

Python中输出JSON最简单的使用就是 `json.dumps(obj)` 这种格式，不过当obj是一个自定义类实例会出现以下的异常：

`TypeError: <__main__.S object at 0x000000000291F7F0> is not JSON serializable`

其实即使obj是一个简单datetime.datetime实例也会出现上述的错误，原因在于在JSON没有与之对应的数据类型（数字、字符串、映射、序列），也不能强制转化，有的人希望得到'2014-11-09 00:00:00'的字符串，也有人希望是1416588374的时间戳，所以直接报错。

以下面自定义User类为例子,某个用户u1 = User('Bob','123456')登录成功后要把他的信息以JSON格式返回给客户端。

<pre><code>
class User(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
</code></pre>

通常我们的做法是

 `json.dumps({'name':u1.name,'pwd':u1.pwd})`，

上述过程中实际我们把自定义类首先转化为一个字典，用函数 `user2dict(u)`表示，这个字典JSON是可以序列化的。所以代码也就是

`json.dumps(user2dict(u))`

那么现在的问题就是，只有一个User类还好办，直接硬编码过去，要是有很多种类，硬编码可就不行了，必须把 `user2dict ` 变成更有通用性的 `obj2dict`。

从 `obj2dict(obj)` 代码可知，如果obj没有__dict__属性，就认为它是基本类型，直接返回，否则遍历所有{属性：值}对，如果是值是list的话，每个元素调用自身obj2dict再组成list，否则直接再调用自身。

`obj2dict` 函数写完之后，一种用法是 `json.dumps(obj2dict(obj))`，看起来很别扭，还有一种可以考虑装饰器，就是这样子，但这样有个问题，json是内置的库不好修改。

其实JSON库有相关的参数，dumps完整声明如下：

`json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)`

参数很多，但default参数和我们上述有关，该方法的描述如下：

> default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.

上面写的obj2dict函数其实就是default回调的一种实现，只不过这里的 a serializable version是个字典，你完全也可以写个类似obj2list的函数，不过那样子可读性非常差了。

所以我们只需要这样子：

`json.dumps(obj, default=obj2dict)`

## 代码

### obj2json模块

```
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
```

### 使用例子

```
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
```
