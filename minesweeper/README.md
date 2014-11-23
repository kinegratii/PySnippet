# Minesweeper（扫雷）

这是一个由Python编写的扫雷游戏，包含了两大部分：游戏算法和GUI界面。

## 算法

游戏算法总体为一个有限状态机。一共有游戏中、成功、失败，其中后两种为最终状态。状态转化为点击某个方格。

游戏的动作是点击某个方格，有三种情况

* 点到已经被点过的，无任何改变，可以继续游戏
* 点到地雷，游戏失败
* 点到本身不是地雷
 * 周围没有地雷，需要继续点开一大片地图（用个队列广度遍历搞定）
 * 周围有地雷的，此时如果没有被点过的数目等于地雷数，游戏成功，否则继续游戏


## GUI

这是由内置tkinter库编写的，主要是按钮的响应函数。为(x,y)处的按钮绑定左键、右键点击事件处理函数的代码：

（x,y）处左键点击函数

<pre><code>
self.bt_map[x][y] = tk.Button(self.map_frame,text='',command = lambda x=x,y=y:self._on_click(x,y))
<code></pre>

(x,y)处右键点击函数，采用闭包形式将x,y传入响应函数

```python            
def right_click_handler(event, self=self, x=x, y=y):
    return self._on_right_click(event, x, y)
self.bt_map[x][y].bind('<Button-3>', right_click_handler)
```