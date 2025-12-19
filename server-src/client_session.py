import json
import socket
from typing import Tuple
from client_manager import ClientManager
from message_handler import MessageHandler
from config import ENCODING, BUFFER_SIZE

class ClientSession:
    def __init__(
        self,
        client_socket: socket.socket,
        address: Tuple[str, int],
        clients: ClientManager,
        handler: MessageHandler,
    ) -> None:
        self.client_socket = client_socket
        self.address = address
        self.clients = clients
        self.handler = handler

    def run(self) -> None:
        print(f"New connection from {self.address}")
        self.clients.add_client(self.client_socket)

        try:
            while True:
                raw = self.client_socket.recv(BUFFER_SIZE)
                if not raw:
                    break
                try:
                    payload = json.loads(raw.decode(ENCODING))
                    self.handler.process_payload(payload, self.client_socket)
                except json.JSONDecodeError:
                    print("Invalid JSON received")
        except OSError:
            pass
        finally:
            print(f"Connection closed: {self.address}")
            self.clients.remove_client(self.client_socket)
            self.client_socket.close()

