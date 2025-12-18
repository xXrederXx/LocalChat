from customtkinter import *


class Chat(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
    def add_msg(self, msg:str):
        label = CTkLabel(self, text=msg, anchor="w", wraplength=800)
        label.pack(fill="both", padx=12)
