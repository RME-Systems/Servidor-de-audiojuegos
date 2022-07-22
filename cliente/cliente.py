#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket
import constantes
from cytolk import tolk
tolk.load()

try:
    raw_input
except NameError:
    raw_input = input


def main():
    s = socket()
    s.connect((constantes.Direccion, constantes.Puerto))
    
    while True:
        output_data = raw_input("> ")
        
        if output_data:
            # Enviar entrada. Comptabilidad con Python 3.
            try:
                s.send(output_data)
            except TypeError:
                s.send(bytes(output_data, "utf-8"))
            
            # Recibir respuesta.
            input_data = s.recv(1024)
            if input_data:
                datos = input_data.decode("utf-8")
                tolk.output("Verbalizo: "+datos)
                


if __name__ == "__main__":
    main()