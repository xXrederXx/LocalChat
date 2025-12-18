from customtkinter import *
from .headercls import Header
from .footercls import Footer
from .chatcls import Chat
from gui.appcls import App

class Window(CTk):
    def __init__(self, app: App):
        super().__init__()
        self.app = app

        self.geometry("800x600")
        self.columnconfigure((0), weight=1)
        self.rowconfigure((1), weight=1)

        self.header = Header(self, app)
        self.header.grid(row=0, column=0, sticky=NSEW)

        self.chat = Chat(self)
        self.chat.grid(row=1, column=0, sticky=NSEW, pady=16)

        self.footer = Footer(self, app)
        self.footer.grid(row=2, column=0, sticky=NSEW)
