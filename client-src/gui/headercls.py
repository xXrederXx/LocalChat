from customtkinter import *
from gui.appcls import App


class Header(CTkFrame):
    def __init__(self, master, app: App):
        super().__init__(master, height=50)
        self.app: App = app

        self.rowconfigure((0, 1), weight=1)

        self.adress_input = CTkEntry(
            self, width=300, height=32, placeholder_text="ip:port"
        )
        self.adress_input.grid(row=0, column=0, sticky="NSWE", padx=4, pady=4)

        self.submit_btn = CTkButton(
            self, width=200, height=32, text="connect", command=self.connect
        )
        self.submit_btn.grid(row=0, column=1, sticky="NSWE", padx=4, pady=4)

    def connect(self):
        input = self.adress_input.get().split(":")
        if len(input) != 2:
            print("Invalid input: use ip:port")
            return

        host = input[0]
        port = 0

        try:
            port = int(input[1])
        except Exception:
            print("Port could not be parsed: " + input[1])

        self.app.connect_to_server((host, port))
