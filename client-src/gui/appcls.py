import socket
import threading
import json


class App:
    def __init__(self):
        from gui.window import Window
        self.window: Window = Window(self)
        self.socket: socket.socket | None = None
        self.ENCODING = "utf-8"
        self.name = str(self.socket.__hash__())
        
        self.window.mainloop()


    def send_msg(self, msg: str):
        if self.socket is None:
            print("No Connection")
            return

        msg = msg.strip()

        if msg.startswith("/setname "):
            self.name = msg.replace("/setname ", "")

        # COMMAND
        if msg.startswith("/"):
            parts = msg[1:].split()
            cmd = parts[0]
            args = parts[1:]

            payload = {
                "type": "cmd",
                "cmd": cmd,
                "args": args,
                "sender": {
                    "name": self.name
                }
            }

        # NORMAL MESSAGE
        else:
            payload = {
                "type": "msg",
                "msg": msg,
                "sender": {
                    "name": self.name
                }
            }

        data = json.dumps(payload).encode(self.ENCODING)
        self.socket.send(data)

    def reveive_msg(self, msg: str):
        payload = json.loads(msg)

        self.window.chat.add_msg(payload["msg"], payload["sender"]["name"], payload["type"] == "p-msg", self.name)

    def msg_listener(self):
        while True:
            try:
                if self.socket == None:
                    continue

                message = self.socket.recv(1024).decode(self.ENCODING)
                if not message:
                    break
                self.reveive_msg(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def connect_to_server(self, connection: tuple[str, int]):
        print(f"Try connect: {connection}")
        if self.socket != None:
            self.socket.close()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect(connection)
            print("Connected to the chat server.")

            # Thread für Empfang der Nachrichten
            threading.Thread(target=self.msg_listener, daemon=True).start()

        except Exception as e:
            print(f"Error connecting to server: {e}")
