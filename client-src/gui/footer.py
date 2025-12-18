from customtkinter import *


class Footer(CTkFrame):
    def __init__(self, master):
        super().__init__(master, height= 50)
        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)

        msg_input = CTkEntry(self, height=32, placeholder_text="message")
        msg_input.grid(row=0, column=0, sticky="NSWE", padx=4, pady=4)

        submit_btn = CTkButton(self, height=32, text="send")
        submit_btn.grid(row=0, column=1, sticky="NSWE", padx=4, pady=4)
