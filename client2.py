import socket

comms_socket = socket.socket()
comms_socket.connect(("120.79.26.97",55001))

while True:
    print(comms_socket.recv(4096).decode("UTF-8"))
    send_data = input("messge: ")
    comms_socket.send(bytes(send_data,"UTF-8"))
