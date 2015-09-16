from socket import *
import os.path, time
import threading

filename = os.path.expanduser("~/file.txt")
IPS = ["10.0.0.10", "10.0.0.11", "10.0.0.12"]

file_lock = threading.Lock()

def readfile(file):
    with file_lock:
        with open(filename, "r") as input_file:
            return input_file.read()


def send():
    last_modified = None
    port = 55567
    buf = 1024

    while True:
        try:
            modified = time.ctime(os.stat(filename).st_mtime)
        except Exception:
            continue
        #If file is modified, sends contents of file to all servers in list of IP addresses
        if (not last_modified or last_modified < modified):
            last_modified = modified
            data = readfile(filename)
            for ip in IPS:
                addr = (ip, port)
                try:
                    clientsocket = socket(AF_INET, SOCK_STREAM)
                    clientsocket.connect(addr)
                    clientsocket.send(data)
                    clientsocket.close()
                except Exception:
                    continue

#Updates file if client sends integer larger than integer already in file
def handler(clientsocket, clientaddr):
    while True:
        data = clientsocket.recv(1024)
        if not data:
            break
        myData = readfile(filename)
        try:
            myData = float(myData)
            try:
                data = float(data)
            except Exception:
                myData = str(myData)
        except Exception:
            pass
        if data > myData:
            with file_lock:
                with open(filename, "w") as output_file:
                    if data > myData:
                        output_file.write(str(data))
    clientsocket.close()

def receive():
    port = 55567
    buf = 1024

    addr = ('', port)

    serversocket = socket(AF_INET, SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(len(IPS))

    while True:
	    clientsocket, clientaddr = serversocket.accept()
	    thread = threading.Thread(target=handler, args=(clientsocket, clientaddr))
	    thread.start()
    serversocket.close()

def main():
    sender = threading.Thread(target=send,name="Sender")
    receiver = threading.Thread(target=receive,name="Receiver")
    receiver.start()
    sender.start()

if __name__ == "__main__":
    main()
