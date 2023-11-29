import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_verify_locations(cafile="server.crt")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_client_socket = context.wrap_socket(client_socket, server_hostname="localhost")

secure_client_socket.connect(('localhost', 8443))
secure_client_socket.sendall(b"Hello, server!")

data = secure_client_socket.recv(1024)
print(f"received {data}")

secure_client_socket.close()
