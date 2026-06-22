import socket   #important to import sockets to use the socket funcions and Network Stuff

ip = "196.168.5.248"    #assign the IP
port = 1

for port in range(1,65536):    #What this part does is assign port the value of range for each round
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, port))

    if resultado == 0:  #If there is a connection, the port is open
        print(f"Opened Port {port}")
    else:
        print(f"Closed Port {port}")

    s.close()

