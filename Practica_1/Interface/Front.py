#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 22/08/2018
@author: f@lv
@author: al3xis
"""

from Tkinter import *


def inicia_ventana(matriz_colores):
    
#=============================================================== VENTANA ===========================================================#
    
    ventana = Tk()
    ventana.title('Matriz de colores')
    ventana.minsize(780,730)
    ventana.maxsize(780,730)
    ventana.config(bg="gray85")

    def pinta_matriz(lista):
        a = 0
        for columna in lista:
            aux = 0
            hgt = 45/len(lista)
            for fila in columna:
                lbl = Label(ventana,width = "24",height = str(hgt),bg = fila,relief="groove")
                lbl.grid(row = a,column = aux)
                aux += 1
            a += 1
    
    
    
    pinta_matriz(matriz_colores)
        
    ventana.mainloop() 


if __name__ == '__main__':
    
    inicia_ventana([["blue","blue","blue","blue"],["cyan","cyan","cyan","cyan"],["gray","gray","gray","gray"],["red","red","red","red"],["gray","gray","gray","gray"],["red","red","red","red"]])
    
    