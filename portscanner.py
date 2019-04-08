import socket
import argparse
# Derived from https://pythonprogramming.net/python-port-scanner-sockets/

def scan(website):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    ports = (23,20,22,25,80,143,443)
    for port in ports:
        print("Testing port ", port)
        if portscan(port,s,website):
            print('Port ',port,' is open')	
    
def portscan(port,s,website):
    try:
        con = s.connect((website,port))
        return True
    except Exception as e:
        print(e)
        return False
 

def main():
    parser = argparse.ArgumentParser(description='Performs a port scan.')
    parser.add_argument('website', help='A website to scan.')
    args = parser.parse_args()
    scan(args.website)

main()