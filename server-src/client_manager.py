import socket
import random
import threading
from typing import Dict, Optional

class ClientManager:
    def __init__(self) -> None:
        self._clients: Dict[socket.socket, str] = {}
        self._lock = threading.Lock()

    def add_client(self, client: socket.socket) -> None:
        with self._lock:
            self._clients[client] = f"NEW USER {random.randint(0, 9999)}"

    def remove_client(self, client: socket.socket) -> None:
        with self._lock:
            self._clients.pop(client, None)

    def set_name(self, client: socket.socket, name: str) -> None:
        with self._lock:
            self._clients[client] = name

    def get_name(self, client: socket.socket) -> Optional[str]:
        return self._clients.get(client)

    def get_all_names(self) -> list[str]:
        return list(self._clients.values())

    def get_all_clients(self) -> list[socket.socket]:
        return list(self._clients.keys())
