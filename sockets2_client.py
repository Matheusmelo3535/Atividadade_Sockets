import socket

HOST = "127.0.0.1"
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Teste do socket, oi oi oi")
    data = s.recv(1024)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket2:
    socket2.connect((HOST, PORT))
    socket2.sendall(b"Dijkstra Dijkstra Dijkstra")
    data2 = socket2.recv(1024)
    
print(f"Received {data!r}")
print(f"Received {data2!r}")