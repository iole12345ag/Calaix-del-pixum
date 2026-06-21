import socket

ip = "196.168.5.248"
puerto= 1

for puerto in range(444,65536):    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, puerto))

    if resultado == 0:
        print(f"Puerto abierto {puerto}")
    else:
        print(f"Puerto cerrado {puerto}")

    s.close()

