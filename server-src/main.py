import json
import random
import socket
import threading
from typing import Dict, Tuple

HOST = "127.0.0.1"
PORT = 6776
ENCODING = "utf-8"

clients: Dict[socket.socket, str] = {}


def broadcast(message: str, sender_socket: socket.socket) -> None:
    prefix = f"{clients[sender_socket]} > "
    print("BRODCAST")
    for client in list(clients.keys()):
        if client is not sender_socket:
            try:
                client.send((prefix + message).encode(ENCODING))
            except OSError:
                client.close()
                clients.pop(client, None)


def handle_command(data: dict, sender_socket: socket.socket) -> None:
    cmd = data.get("cmd")
    args = data.get("args", [])

    if cmd == "setname" and args:
        old = clients[sender_socket]
        new = args[0]
        clients[sender_socket] = new
        print(f"USER UPDATE NAME (OLD: {old} NEW: {new})")

    elif cmd == "active":
        message = "ACTIVE USERS:\n"
        message += "\n".join(f"\t{name}" for name in clients.values())
        sender_socket.send(message.encode(ENCODING))


def process_payload(payload: dict, sender_socket: socket.socket) -> None:
    print(f"PAYLOAD INCOMING {payload}")
    msg_type = payload.get("type")

    if msg_type == "msg":
        message = payload.get("msg")
        if message:
            broadcast(message, sender_socket)

    elif msg_type == "cmd":
        handle_command(payload, sender_socket)


def handle_client(client_socket: socket.socket, client_address: Tuple[str, int]) -> None:
    print(f"New connection from {client_address}")
    clients[client_socket] = f"NEW USER {random.randint(0, 9999)}"

    try:
        while True:
            raw = client_socket.recv(1024)
            if not raw:
                break

            try:
                payload = json.loads(raw.decode(ENCODING))
                process_payload(payload, client_socket)
            except json.JSONDecodeError:
                print("Invalid JSON received")

    except OSError:
        pass
    finally:
        print(f"Connection closed: {client_address}")
        clients.pop(client_socket, None)
        client_socket.close()


def start_server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
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
