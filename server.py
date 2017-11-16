import socket

comms_socket1 = socket.socket()
comms_socket2 = socket.socket()
comms_socket1.bind(("120.79.26.97",55000))
comms_socket2.bind(("120.79.26.97",55001))
comms_socket1.listen()
user1,address1 = comms_socket1.accept()
comms_socket2.listen()
user2,address2 = comms_socket2.accept()

while True:
    send_date = user1.recv(4096).decode("UTF-8")
    user2.send(bytes(send_data,"UTF-8"))
    send_date = user2.recv(4096).decode("UTF-8")
    user1.send(bytes(send_data,"UTF-8"))

