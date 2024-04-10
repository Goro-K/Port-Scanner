import socket

# Function to get all the information about the IP address (host, alias, IP)
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

print ("Scanning host: " + str(host[0])) 

# Port scanner

try:
    for port in range(65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print ("Port {} is open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Exiting program")
    exit()

except socket.error:
    print("Could not connect to server")
    exit()