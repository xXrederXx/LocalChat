import json
from config import ENCODING


def generate_msg(msg: str, sender_name: str) -> bytes:
    payload = {
        "type": "msg",
        "msg": msg,
        "sender": {
            "name": sender_name
        }
    }
    return json.dumps(payload).encode(ENCODING)

def generate_private_msg(msg: str, sender_name: str) -> bytes:
    payload = {
        "type": "p-msg",
        "msg": msg,
        "sender": {
            "name": sender_name
        }
    }
    return json.dumps(payload).encode(ENCODING)
