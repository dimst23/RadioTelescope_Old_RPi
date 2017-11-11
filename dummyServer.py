import socket

host = "localhost"
port = 10001

address = (host, port)

sock = socket.socket()
sock.bind(address)
sock.listen(1)

client, addr = sock.accept()
print(addr)
discon = False

while(True):
    if discon:
        client, addr = sock.accept()
        discon = False
    rcv = client.recv(1024).decode('utf-8')
    
    if rcv == "Test":
        client.send(("OK").encode('utf-8'))
        print("\'OK\' was sent to client as a response.")
        continue
    elif rcv == "Terminate":
        client.send(("Bye").encode('utf-8'))
        client.close()
        print("\'Bye\' was sent to client as a response and connection was terminated")
        discon = True
        continue
    elif rcv == "":
        print("Client disconnected without notice.")
        break
    print("Client sent: %s" %rcv)
    ch = input("Enter the message to be sent:" )
    client.send(ch.encode('utf-8'))
    print("\'%s\' was sent to client as a response." %ch)
