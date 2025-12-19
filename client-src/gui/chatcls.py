from customtkinter import *


class Chat(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
    def add_msg(self, msg:str, sender:str, is_private:bool, myname:str):
        anchor = "e" if sender == myname else "w"
        text_color = "orange" if is_private else ("black", "white")

        chat_box = CTkFrame(self)

        name_label = CTkLabel(chat_box, text=sender, anchor=anchor, wraplength=800, text_color=text_color)
        name_label.pack(fill="both", padx=6)

        msg_bubble = CTkFrame(chat_box, bg_color="transparent", fg_color=("#ebebeb", "#2f333a"), corner_radius=8)
        msg_bubble.pack(padx=6, anchor=anchor)

        msg_label = CTkLabel(msg_bubble, text=msg, anchor=anchor, wraplength=800, text_color=text_color)
        msg_label.pack(fill="both", padx=12, pady=6)

        chat_box.pack(fill="both", padx=12, pady=6)

        # Scroll to bottom (https://stackoverflow.com/questions/78359834/scroll-function-for-ctkscrollableframe-python)
        self.update_idletasks()
        self._parent_canvas.yview_moveto(1.0)
