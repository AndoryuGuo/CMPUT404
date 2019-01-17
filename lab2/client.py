#!urs/bin/env python3
import socket

HOST = "www.google.com"
PORT = 80

payload = '''GET / HTTP/1.0
HOST: {HOST}

'''.format(HOST=HOST)

BUFFER_SIZE = 1024

def connect_socket(addr):
    (family, socktype, proto, cannomano, sockaddr) = addr
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        print("CONNECTED")
        s.sendall(payload.encode())
        fulldata = b''
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            fulldata += data
        print(fulldata)
    except:
        print("CONNECTION FAILED")
        pass
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.IPPROTO_TCP)
    addr = addr_info[0]
    connect_socket(addr)

if __name__ == '__main__':
    main()