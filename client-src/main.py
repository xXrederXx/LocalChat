import socket
import threading

HOST = "127.0.0.1"  # IP des Servers
PORT = 9999  # Port des Servers (> 1023)

# Funktion, um empfangene Nachrichten zu verarbeiten
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Einstiegspunkt
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to the chat server.")

        # Thread für Empfang der Nachrichten
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        while True:
            message = input()
            if message.lower() == 'quit':
                print("Exiting chat...")
                break
            client_socket.send(message.encode('utf-8'))

    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
