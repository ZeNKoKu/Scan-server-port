import socket
import time
import sys,os

print("Projet By JT Pentester")
print("https://github.com/RattanachatJTPentester")
print("I have fixed this program")
print("")
print("github me")
print("https://github.com/ZeNKoKu")

server = input("IP : ")
print("IP:"+server)
print("in progress.")
time.sleep(2)
print("in progress..")
time.sleep(2)
print("in progress...")
time.sleep(2)
def scan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((server,port))
        return True
    except:
        return False

for port in range(1,26):
    if scan(port):
        print(f'Port {port} is open')
    else:
        print("no open ports")
        pass

os.system("ping "+server)
print("")    
time.sleep(5)
os.system("clear")
print("ThX na kub")
