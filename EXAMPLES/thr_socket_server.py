#!/usr/bin/env python

import socket
import threading


class ClientHandler(threading.Thread):
    '''A thread to handle one client request'''

    def __init__(self, client_socket, client_address):
        super(ClientHandler, self).__init__()
        self._client_socket = client_socket
        self._client_address = client_address

    def run(self):  # <1>
        request = self._client_socket.recv(1024)  # <2>

        reply = request.upper()[::-1]  # <3>

        self._client_socket.sendall(reply)  # <4>
        self._client_socket.close()  # <5>


def setup():
    '''Initialize the server socket'''
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # <6>
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <7>
    # serv.setblocking(0)

    serv.bind((socket.gethostname(), 7777))  # <8>
    serv.listen(5)  # <9>

    return serv


def main():
    '''Main program.'''
    serv = setup()
    while True:  # <10>
        (csock, addr) = serv.accept()  # <11>
        handler = ClientHandler(csock, addr)  # <12>
        handler.start()  # <13>


if __name__ == '__main__':
    main()
