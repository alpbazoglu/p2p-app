import json
import socket

LISTEN_IP = '0.0.0.0'
BROADCAST_PORT = 5001
BUFFER_SIZE = 65535
TARGET_EXTENSION = ''  # Sadece belirli bir uzantıya sahip dosyaları taramak için değiştirin

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, BROADCAST_PORT))

content_dictionary = {}

def main():
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = json.loads(data.decode('utf-8'))

        files = message.get('chunks', [])

        for file in files:
            if file.endswith(TARGET_EXTENSION):  # Sadece hedef uzantıya sahip dosyaları ekleyin
                if file not in content_dictionary:
                    content_dictionary[file] = [addr[0]]
                    print(f"Yeni içerik algılandı: {addr[0]} : {file}")
                elif addr[0] not in content_dictionary[file]:
                    content_dictionary[file].append(addr[0])
                    print(f"{file} için yeni IP adresi algılandı: {addr[0]}")

        with open('content_dictionary.txt', 'w') as f:

            f.write(json.dumps(content_dictionary, indent=4))
            f.flush();

if __name__ == "__main__":
    main()