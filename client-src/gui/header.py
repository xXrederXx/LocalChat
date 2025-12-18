from customtkinter import *


class Header(CTkFrame):
    def __init__(self, master):
        super().__init__(master, height= 50)
        self.rowconfigure((0, 1), weight=1)

        adress_input = CTkEntry(self, width=300, height=32, placeholder_text="ip:port")
        adress_input.grid(row=0, column=0, sticky="NSWE", padx=4, pady=4)

        submit_btn = CTkButton(self, width=200, height=32, text="connect")
        submit_btn.grid(row=0, column=1, sticky="NSWE", padx=4, pady=4)
