from customtkinter import *


class Chat(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
    def add_msg(self, msg:str, sender:str, isprivate:bool, myname:str):
        anchor = "e" if sender == myname else "w"
        text_color = "orange" if isprivate else ("black", "white")

        chat_box = CTkFrame(self)

        name_label = CTkLabel(chat_box, text=sender, anchor=anchor, wraplength=800, text_color=text_color)
        name_label.pack(fill="both", padx=6)

        msg_bubble = CTkFrame(chat_box, bg_color=("#ebebeb", "#2f333a"), fg_color=("#ebebeb", "#2f333a"), corner_radius=8)
        msg_bubble.pack(padx=6, anchor=anchor)

        msg_label = CTkLabel(msg_bubble, text=msg, anchor=anchor, wraplength=800, text_color=text_color)
        msg_label.pack(fill="both", padx=12, pady=6)

        chat_box.pack(fill="both", padx=12, pady=6)
