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

`obj2dict` 函数写完之后，一种用法是 `json.dumps(obj2dict(obj))`，看起来很别扭，还有一种可以考虑装饰器，但有个问题json是内置的库不好修改。

其实JSON库已经考虑了这个问题，dumps完整声明如下：

`json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)`

参数很多，但cls参数和我们上述有关，看看它的定义，cls的值必须继承于 `JSONEncoder` 这个类，而且要重写一个default(0)的方法，该方法的描述如下：

> default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.

这个default的方法就是上面实现了的obj2dict，只不过这里的 a serializable version是个字典，你完全也可以写个类似obj2list的函数，不过那样子可读性非常差了。

## 后续

### 序列化

* 现在是一个比较简单的样子，还有一些更加高级的内容，比如只需输出部分字段，字符串格式化、自定义键名称等等。

* 关于嵌套对象的序列化也有去了解Django的一些源码，基本思想是一致的，只不过把递归部分放在数据转化里面，因为它还需要其他序列化其他格式。

### 反序列化

* 关于反序列化，既然有序列化，怎么能没有反序列化呢，后来发现还是不写了。也试着写了一些代码，按照上面写了个相反的函数 `dict2obj（dict,cls）`，想按照同样的方法套在 `load` 方法上，才发现参数不一致！！ `object_hook` 和 `object_hooks` 没有cls参数，要么在dict数据中，要么在回调函数直接硬编码。有想过用装饰器把 `dict2obj`包一层，将cls作为函数的参数，不过这好像对递归函数又有些问题。

* 序列化和反序列化是相反的过程，应该相互考虑对方的“感受”。上面的序列化的做法就像只顾自己的一样，自己输出的数据根本不打算还原回来，这也是反序化写着比较费劲的原因之一吧。



### 作者

By Kinegratii