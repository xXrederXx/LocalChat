from customtkinter import *
from .header import Header
from .footer import Footer
from .chat import Chat


class Window(CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.columnconfigure((0), weight=1)
        self.rowconfigure((1), weight=1)
        
        header = Header(self)
        header.grid(row=0, column=0, sticky=NSEW)
        
        chat = Chat(self)
        chat.grid(row=1, column=0, sticky=NSEW, pady=16)

        footer = Footer(self)
        footer.grid(row=2, column=0, sticky=NSEW)