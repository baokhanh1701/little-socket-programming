import socket
from threading import Thread

# class ThreadWithReturn(Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
#         Thread.__init__(self, group, target, name, args, kwargs)
#         self._return = None # parameter for later return value
    
#     # Override the invoker run() to pass callable object
#     def run(self):
#         if self._target is not None:
#             self._return = self._target(*self._args, **self._kwargs)
    
#     # Override value passing
#     def join(self, *args):
#         Thread.join(self, *args)
#         return self._return

#! implement this shit
# def register_port(hostname, port_num=5000):

def Client():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

# ...
# binder = Thread(target=register_port, args=(host, port))
# binder.start()

if __name__ == '__main__':
    Client()