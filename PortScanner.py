# Port Scanner. Created By Milad Zadeh Mousavi

import socket
import sys

answer = "yes"

while answer == "yes" or answer == "y":

    print("-" * 60)
    Dname = input("Please type Target Ip or Hostname to Scanning:")
    print("-" * 60)

    if Dname == "":
        print("please type agani :")
    else:
        print("your Target is: ", Dname)

        print("-" * 60)

        try:
            name, aliases, addresses = socket.gethostbyname_ex(Dname)
            print('  Hostname:', name)
            print('  Aliases :', aliases)
            print(' Addresses:', addresses)
            print("-" * 60)

        except socket.error as msg:
            print('ERROR:', msg)

    answer = input("do you want try again? :")

print("==> Coder: Milad Zadeh Mousavi <==")
sys.exit()
