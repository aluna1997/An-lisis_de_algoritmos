#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 22/08/2018
@author: f@lv
@author: al3xis
"""

def inicia_dict_colores():
    
    colores ={ "0000" : "cyan",
               "0001" : "spring green",
               "0010" : "gold",
               "0011" : "navajo white",
               "0100" : "purple1",
               "0101" : "coral1",
               "0110" : "HotPink1",
               "0111" : "brown1",
               "1000" : "cornflower blue",
               "1001" : "light grey",
               "1010" : "Khaki1",
               "1011" : "LightBlue1",
               "1100" : "thistle1",
               "1101" : "orange2",
               "1110" : "LightPink1",
               "1111" : "salmon1"
    }
    
    return colores


def genera_matriz_colores(cadena):
    """
    Función que recibe una cadena y regresa una matriz con el identificador de
    un color en cada celda.
    """
    colores = inicia_dict_colores()
    columnas = []
    fila = []
    for i in cadena:
        fila.append(colores[map(bin,bytearray(i))[0].replace("b", "")[0:4]])
        if len(map(bin,bytearray(i))[0].replace("b", "")[4:]) >= 4:
            fila.append(colores[map(bin,bytearray(i))[0].replace("b", "")[4:8]])
        else:
            fila.append(colores[map(bin,bytearray(i))[0].replace("b", "")[4:8]  + "0"])
            
        if len(fila) == 4:
            columnas.append(fila)
            fila = []
    return columnas


if __name__ == "__main__":
    
    #print genera_matriz_colores("AaNm")
    
    print map(bin,bytearray("¡"))[0].replace("b", "")[4:8]
   
