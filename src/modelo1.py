import numpy as np
import parametros as p

def Modelo_Ideal(t):
    return int(t / p.ciclo_maquina)