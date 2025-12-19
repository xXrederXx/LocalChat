import socket
import threading
from client_manager import ClientManager
from message_handler import MessageHandler
from client_session import ClientSession
from config import HOST, PORT, SERVER_NAME
import payload_generator as pg

class ChatServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.clients = ClientManager()
        self.handler = MessageHandler(self.clients)

    def start(self) -> None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        server_socket.settimeout(1.0)  # Allows Ctrl+C to work

        print(f"Server listening on {self.host}:{self.port}")

        try:
            while True:
                try:
                    client_socket, address = server_socket.accept()
                    session = ClientSession(
                        client_socket,
                        address,
                        self.clients,
                        self.handler,
                    )
                    threading.Thread(target=session.run, daemon=True).start()
                except socket.timeout:
                    continue
        except KeyboardInterrupt:
            self.handler.broadcast(pg.generate_msg("SERVER SHUTTING DOWN", SERVER_NAME))
            print("Server shutting down...")
        finally:
            server_socket.close()


if __name__ == "__main__":
    ChatServer(HOST, PORT).start()
