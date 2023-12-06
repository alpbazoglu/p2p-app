import os
import socket
import json
import time

CHUNK_SIZE = 1024  # Değiştirmeniz gereken boyut
BROADCAST_IP = '255.255.255.255'
BROADCAST_PORT = 5001

def divide_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        file_size = len(data)
        chunk_count = 5  # Parça sayısı 5 olarak sabitlendi
        chunk_size = file_size // chunk_count
        remaining_bytes = file_size % chunk_count

        chunks = []
        start = 0
        for i in range(chunk_count):
            end = start + chunk_size
            if i < remaining_bytes:
                end += 1
            chunk = data[start:end]
            chunks.append(chunk)
            start = end

        for i, chunk in enumerate(chunks):
            with open(f'{file_path[:-4]}_{i+1}', 'wb') as chunk_file:
                chunk_file.write(chunk)

        return len(chunks)

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def broadcast_files(directory):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        file_list = list_files(directory)
        message = json.dumps({'chunks': file_list}).encode('utf-8')
        sock.sendto(message, (BROADCAST_IP, BROADCAST_PORT))
        time.sleep(2)  # Bir dakikada bir yayınla

def main():
    file_path = input('Lütfen paylaşmak istediğiniz dosyayı belirtin: ')
    directory = os.path.dirname(file_path)
    if directory == '':
        directory = '.'
    chunk_count = divide_file(file_path)
    print(f'{chunk_count} parça oluşturuldu. Dosyaları duyurmak için yayınlamaya başlanıyor...')
    broadcast_files(directory)

if __name__ == "__main__":
    main()