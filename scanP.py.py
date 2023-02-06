#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText('Port scanner'))


def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")
        sock.close()
    return open_ports


try:
    host = input("Enter the host IP address: ")
    start_port = int(input("Enter the start of the port range: "))
    end_port = int(input("Enter the end of the port range: "))
    scan_ports(host, start_port, end_port)
except KeyboardInterrupt:
    exit()
except ValueError:
    print("Only integer value for port")


