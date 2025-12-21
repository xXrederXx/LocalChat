from customtkinter import CTkFrame, CTkEntry, CTkButton
from gui.appcls import App


class Footer(CTkFrame):
    def __init__(self, master, app: App):
        super().__init__(master, height=50)
        self.app = app

        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)

        self.msg_input = CTkEntry(self, height=32, placeholder_text="message")
        self.msg_input.grid(row=0, column=0, sticky="NSWE", padx=4, pady=4)

        self.submit_btn = CTkButton(self, height=32, text="send", command=self.send_msg)
        self.submit_btn.grid(row=0, column=1, sticky="NSWE", padx=4, pady=4)
    
    def send_msg(self):
        input = self.msg_input.get()
        self.app.send_msg(input)
