#!urs/bin/env python3
import socket

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsock
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        full_data = b''
        with conn:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data: 
                    break
                full_data += data
            conn.sendall(full_data)


if __name__ == '__main__':
    main()