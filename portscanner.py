import socket
import argparse

def scan(host, ports = None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print (host)
    if ports is None:
      ports = (20,21,22,23,80,88,443,8080)

    for port in ports:

        if portscan(s,host,int(port)):
            print('Port ',port,': Open')
            s.detach()
        else :
            print('Port ',port,': Closed')

def portscan(s,host,port):
    try:
        con = s.connect((host,port))
        return True
    except Exception as e:
        return False


def main():
    parser = argparse.ArgumentParser(description='Performs a port scan.')
    parser.add_argument('-s','--host', help='A host to scan.')
    parser.add_argument('-p','--ports', nargs='*', help='List of ports to scan', required = False)


    args = parser.parse_args()

    scan(args.host,args.ports)

main()
