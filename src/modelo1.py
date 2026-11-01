import numpy as np
import parametros as p

def Modelo_ideal(t):
    return int(t / p.ciclo_maquina)