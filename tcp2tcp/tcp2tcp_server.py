#coding=utf8
"""
程序分别在8059监听上行设备连接请求，在8060监听下行设备连接请求
实现绑定同一端口（设备上的端口）的上下行设备数据相互转发
一个双向的数据流向
(upper_ip,9005) - (server_ip,8059) -  (server_ip,8060) - (lower_ip,9005)

"""
import socket
import SocketServer
import threading

LOCAL_HOST = ''

UPPER_LISTEN_PORT = 8059

LOWER_LISTEN_PORT = 8060


class ConnectionPool(object):
    def __init__(self):
        self.con_dict = {}
        self.lock = threading.Lock()

    def add_connection(self, port, connect):
        self.lock.acquire()
        try:
            self.con_dict[port] = connect
        finally:
            self.lock.release()

    def delete_connection(self, port):
        self.lock.acquire()
        try:
            if port in self.con_dict:
                del self.con_dict[port]
                print 'del connect',port
        finally:
            self.lock.release()

    def get_connection(self, port):
        if port in self.con_dict:
            return self.con_dict[port]
        return None

    def send_data(self, data, port):
        self.lock.acquire()
        try:
            if port in self.con_dict:
                print 'send data'
                connect = self.con_dict[port]
                connect.sendall(data)
                result = True
            else:
                result =  False
        except Exception:
            result = False
        finally:
            self.lock.release()
            return result


class UpperRequestHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        #add this socket to the pool
        client_host, client_port = self.client_address
        print ' upper set up ', client_port
        upper_pool.add_connection(client_port,self.request)

    def handle(self):
        client_host, client_port = self.client_address
        while True:
            try:
                data = self.request.recv(1024)
            except Exception:
                break
            if len(data) > 0:
                lower_pool.send_data(data, client_port)
        lower_pool.delete_connection(client_port)

class LowerRequestHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        #add this socket to the pool
        client_host, client_port = self.client_address
        print ' lower set up ', client_port
        lower_pool.add_connection(client_port, self.request)

    def handle(self):
        client_host, client_port = self.client_address
        while True:
            try:
                data = self.request.recv(1024)
            except Exception:
                break
            if len(data) > 0:
                upper_pool.send_data(data, client_port)
        upper_pool.delete_connection(client_port)



class TCPForwardServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, bind_port, handler):
        SocketServer.TCPServer.__init__(self, (LOCAL_HOST, bind_port), handler)

class TCP2TCPServer(object):
    def __init__(self, upper_port, lower_port):
        self.upper_port = upper_port
        self.lower_port = lower_port
        
    def start(self):
        print 'TCP2TCP Server start success...'
        ut = threading.Thread(target=self.start_upper)
        ut.start()
        lt = threading.Thread(target=self.start_lower)
        lt.start()
        
    def start_upper(self):
        upper_server = TCPForwardServer(self.upper_port, UpperRequestHandler)
        upper_server.serve_forever()

    def start_lower(self):
        lower_server = TCPForwardServer(self.lower_port, LowerRequestHandler)
        lower_server.serve_forever()

upper_pool = ConnectionPool()
lower_pool = ConnectionPool()

def main():
    server = TCP2TCPServer(UPPER_LISTEN_PORT, LOWER_LISTEN_PORT)
    server.start()

if __name__ == '__main__':
    main()
