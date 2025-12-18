import random
import socket
import threading
import numpy
from typing import List, Tuple, Dict

HOST: str = "172.17.103.104"
PORT: int = 6766
ENCODING = "utf-8"

clients: Dict[socket.socket, str] = {}


# Send recived data to all clients
def broadcast(message: bytes, sender_socket: socket.socket) -> None:
    print(f"BROADCAST MESSAGE (msg: {message.decode(ENCODING)})")
    for client, name in clients.items():
        if client is not sender_socket:
            try:
                message = (clients[sender_socket] + " > ").encode(ENCODING) + message
                client.send(message)
            except OSError:
                client.close()
                clients.pop(client)


def process_msg(msg: str, sender_socket: socket.socket) -> str | None:
    if msg.startswith("/name "):
        name = msg.replace("/name ", "")

        print(f"USER UPDATE NAME (OLD: {clients[sender_socket]} NEW: {name}) ")

        clients.update({sender_socket: name})
        return None
    if (msg.startswith("/active")):
        message = "ACTIVE USERS:"
        for client in clients.values():
            message += f"\n\t{client}"
        sender_socket.send(message.encode(ENCODING))
        return None
    return msg


# Starts a new session with a client
def handle_client(
        client_socket: socket.socket,
        client_address: Tuple[str, int]
) -> None:
    print(f"New connection from {client_address}")
    clients[client_socket] = "NEW USER " + str(random.randint(0, 9999))

    try:
        while True:
            message: str | None = client_socket.recv(1024).decode(ENCODING)
            message = process_msg(message, client_socket)
            if not message:
                continue
            broadcast(message.encode(ENCODING), client_socket)
    except OSError:
        pass
    finally:
        print(f"Connection closed: {client_address}")
        clients.pop(client_socket)
        client_socket.close()


def start_server() -> None:
    server_socket: socket.socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket: socket.socket
            client_address: Tuple[str, int]

            client_socket, client_address = server_socket.accept()
            threading.Thread(
                target=handle_client,
                args=(client_socket, client_address),
                daemon=True
            ).start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
