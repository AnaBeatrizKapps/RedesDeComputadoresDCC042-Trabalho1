from os import cpu_count
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
QUIT_MSG = "QUIT"

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(ADDR)
  print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
  

  connected = True
  while connected:
    msg = input("> ")

    # client.send(msg.encode(FORMAT))

    if 'echo' in msg or 'ECHO' in msg:
      client.send(msg.encode(FORMAT))
      msg = client.recv(SIZE).decode(FORMAT)
      print(f"[SERVER] {msg}")
    elif(QUIT_MSG in msg):
      client.send(msg.encode(FORMAT))
      connected = False

if __name__ == "__main__":
  main()