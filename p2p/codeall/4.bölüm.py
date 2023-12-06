import socket
import json
from datetime import datetime

TCP_PORT = 5000

def download_file_chunk(ip_address, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip_address, TCP_PORT))
        message = json.dumps({"requested_content": filename}).encode('utf-8')
        sock.sendall(message)
        chunk_data = sock.recv(1024)
        return chunk_data
    finally:
        sock.close()

def merge_chunks(filename, start_chunk, end_chunk):
    with open("./downloaded/"+filename, 'wb') as output_file:
        for i in range(start_chunk, end_chunk):
            chunk_name = f"{filename[:-4]}_{i+1}"
            with open(chunk_name, 'rb') as chunk_file:
                output_file.write(chunk_file.read())

def main():
    start_chunk = 0
    end_chunk = 5  # 5 dahil değil

    with open('content_dictionary.txt', 'rb') as f:
        content_dictionary = json.load(f)

    filename = input("İndirmek istediğiniz dosyanın adını girin: ")

    for i in range(start_chunk, end_chunk):
        chunk_name = f"{filename[:-4]}_{i+1}"
        if chunk_name not in content_dictionary:
            print(f"CHUNK {chunk_name} ONLINE KAYNAKLARDAN İNDİRİLEMEZ.")
            continue

        for ip_address in content_dictionary[chunk_name]:
            try:
                chunk_data = download_file_chunk(ip_address, chunk_name)
                with open(chunk_name, 'wb') as chunk_file:
                    chunk_file.write(chunk_data)
                print(f"{chunk_name} başarıyla {ip_address} adresinden indirildi.")
                with open('download_log.txt', 'a') as log_file:
                    log_file.write(f"{datetime.now()}: {chunk_name} {ip_address} adresinden indirildi\n")
                break
            except Exception as e:
                print(f"{chunk_name} {ip_address} adresinden indirilemedi: {e}")
        else:
            print(f"CHUNK {chunk_name} ONLINE KAYNAKLARDAN İNDİRİLEMEZ.")

    merge_chunks(filename, start_chunk, end_chunk)

    # Dosyayı sunucuya yükleme işlemini burada gerçekleştirin

    print(f"{filename} dosyasının {start_chunk}-{end_chunk-1} parçaları başarıyla indirildi ve birleştirildi.")

if __name__ == "__main__":
    main()