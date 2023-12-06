import socket
import json
from datetime import datetime

TCP_PORT = 5000
BUFFER_SIZE = 1024
LOG_FILE = 'chunk_upload_log.txt'

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', TCP_PORT)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            data = connection.recv(BUFFER_SIZE)
            message = json.loads(data.decode('utf-8'))
            filename = message.get('requested_content', '')

            with open(filename, 'rb') as f:
                chunk_data = f.read()
                connection.sendall(chunk_data)

            with open(LOG_FILE, 'a') as f:
                log_message = f"Parça adı: {filename}, Zaman damgası: {datetime.now()}, Hedef IP adresi: {client_address[0]}\n"
                f.write(log_message)
        finally:
            connection.close()

if __name__ == "__main__":
    start_server()