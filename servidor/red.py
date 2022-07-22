#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import Cliente
import constantes

def main():
    s = socket()
    
    # Escuchar peticiones en el puerto puerto.
    s.bind((constantes.Escuchar, constantes.Puerto))
    s.listen(0)
    
    while True:
        conexion, direccion = s.accept()
        c = Cliente.Cliente(conexion, direccion)
        c.start()
        


if __name__ == "__main__":
    main()