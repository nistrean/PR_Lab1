import socket
import threading


def broadcast(address, message):
    for client_socket in clients:
        client_socket.send(f"{address}: {message.decode('utf-8')}".encode('utf-8'))


def receive(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024)
            if message.decode('utf-8') == 'exit':
                break
            print(f"{address}: {message.decode('utf-8')}")
            broadcast(address, message)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()
    print(f"{address} a parasit chat-ul.")
    broadcast(address, ' a parasit chat-ul.'.encode('utf-8'))

    if not clients:
        print('Serverul asteapta alte conexiuni...')


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9000))
    server_socket.listen()

    clients = []

    print('Serverul asteapta conexiuni...')

    while True:
        client_socket, address = server_socket.accept()

        print(f"{address} s-a alaturat chat-ului.")
        broadcast(address, 's-a alaturat chat-ului.'.encode('utf-8'))
        clients.append(client_socket)
        client_socket.send('Conectat la server. Introdu ceva text pentru a trimite: '.encode('utf-8'))

        thread = threading.Thread(target=receive, args=(client_socket, address))
        thread.start()
