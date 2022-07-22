#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import socket
import constantes
from cytolk import tolk
tolk.load()
import sys, pygame

try:
    raw_input
except NameError:
    raw_input = input


def main():
    pygame.init()
    ventana = pygame.display.set_mode(constantes.TamanioVentana)
    pygame.display.set_caption(constantes.TituloVentana)

    s = socket()
    s.connect((constantes.Direccion, constantes.Puerto))
    ejecutar=True
    while ejecutar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutar = False
                pygame.time.delay(2)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            s.send(bytes('Hola, mundo','UTF-8'))
            # try:
                # s.send(output_data)
            # except TypeError:
                # s.send(bytes(output_data, "utf-8"))
            
            # Recibir respuesta.
            datos_recibidos = s.recv(1024)
            if datos_recibidos:
                datos = datos_recibidos.decode("utf-8")
                tolk.output("Verbalizo: "+datos)
    exit()


if __name__ == "__main__":
    main()