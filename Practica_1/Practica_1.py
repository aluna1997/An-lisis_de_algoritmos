#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 22/08/2018
@author: f@lv
@author: al3xis
"""

import sys
from Code.Back import genera_matriz_colores
from Interface.Front import inicia_ventana

if __name__ == "__main__":
    
    parametros = sys.argv[1:]
    
    try:
        if len(parametros) == 0:
            print "No hay argumentos"
        elif len(parametros) == 1:
                matriz_colores = genera_matriz_colores(parametros[0])
                inicia_ventana(matriz_colores)
        else:
            print "Número de argumentos incorrecto"
    except:
        print "Ocurrio un error:", sys.exc_info()[0]
        raise   
        
