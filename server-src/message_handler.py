import json
import socket
from client_manager import ClientManager
from config import ENCODING


class MessageHandler:
    def __init__(self, clients: ClientManager) -> None:
        self.clients = clients

    def broadcast(self, message: str, sender: socket.socket) -> None:
        sender_name = self.clients.get_name(sender)
        if not sender_name:
            return
        payload = {
            "type": "msg",
            "msg": message,
            "sender": {
                "name": self.clients.get_name(sender)
            }
        }
        prefix = f"{sender_name} > "
        for client in self.clients.get_all_clients():
            try:
                client.send(json.dumps(payload).encode(ENCODING))
            except OSError:
                client.close()
                self.clients.remove_client(client)

    def handle_command(self, payload: dict, sender: socket.socket) -> None:
        cmd = payload.get("cmd")
        args = payload.get("args", [])

        if cmd == "setname" and args:
            old_name = self.clients.get_name(sender)
            new_name = args[0]
            self.clients.set_name(sender, new_name)
            print(f"USER UPDATE NAME (OLD: {old_name} NEW: {new_name})")

        elif cmd == "active":
            users = "\n".join(f"\t{name}" for name in self.clients.get_all_names())
            message = f"ACTIVE USERS:\n{users}"
            sender.send(message.encode(ENCODING))

    def process_payload(self, payload: dict, sender: socket.socket) -> None:
        msg_type = payload.get("type")

        if msg_type == "msg":
            message = payload.get("msg")
            if message:
                self.broadcast(message, sender)
        elif msg_type == "cmd":
            self.handle_command(payload, sender)
