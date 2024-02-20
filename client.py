import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9000))


def receive_message():
    while True:
        try:
            mesaj = client_socket.recv(1024).decode('utf-8')
            print(mesaj)
        except:
            print('Conexiunea a fost inchisa.')
            break


def write_send_message():
    while True:
        message = input("")
        if message == 'exit':
            client_socket.send(message.encode('utf-8'))
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.shutdown(socket.SHUT_RDWR)
    client_socket.close()


write_thread = threading.Thread(target=write_send_message)
write_thread.start()

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
