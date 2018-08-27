#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 22/08/2018
@author: f@lv
@author: al3xis
"""

from Code.Back import genera_matriz_colores
from Interface.Front import inicia_ventana

if __name__ == "__main__":
    
    cadena = "4B92ZoR1f9TM"
    matriz_colores = genera_matriz_colores(cadena)
    inicia_ventana(matriz_colores)
    
