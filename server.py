import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8443))
server_socket.listen(5)

while True:
    (client_socket, client_address) = server_socket.accept()
    secure_client_socket = context.wrap_socket(client_socket, server_side=True)
    
    data = secure_client_socket.recv(1024)
    print(f"received {data}")
    
    response = b"Hello, client!"
    secure_client_socket.sendall(response)
    
    secure_client_socket.close()
