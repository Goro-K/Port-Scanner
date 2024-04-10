import socket

def adressInfo(ip):
    try:
        return socket.gethostbyaddr(ip)
    except socket.herror:
        return "No host found"
    
def askForIP():
    try:
        return input("Enter the IP address: ")
    except ValueError:
        return "Invalid IP address"

ip = askForIP()
host = adressInfo(ip)

for port in range(65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print("Port " + str(port) + " is open")
    sock.close()

print("Host: " + str(host))