# TCP双向数据中转器

## 简介

这是之前为硬件部门写的一个小工具。

程序分别在8059监听上行设备连接请求，在8060监听下行设备连接请求，实现绑定同一端口（设备上本地的端口）的上下行设备数据的相互转发。

一个双向的数据流向如下：

(upper\_ip, 9005) - (server\_ip, 8059) -  (server\_ip, 8060) - (lower\_ip, 9005)

## 使用

### tcp2tcp_server.py

服务器脚本，在服务器运行 `python tcp2tcp_server.py`即可

### mock_device.py

模拟设备，命令行格式 `python mock_device.py remote_address connect_port mode`

各参数意义如下：

* remote_address：服务器地址

* connect_port： 远程服务器连接端口，即8059或8060

* mode：工作模式，read数据接收方，send数据发送方

在计算机P1中用 `python mock_device.py 192.168.1.9 8059 read` 模拟一个9005上行接收设备，

在计算机P2用 `python mock_device.py 192.168.1.9 8060 send` 模拟一个9005下行发送设备，

则数据流向为 P2 - P1



## 作者

Kinegratii <kinegratii@gmail.com>
