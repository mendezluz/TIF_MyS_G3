import numpy as np
import parametros as p

def Modelo_humano(T, maquinas):

  np.random.seed(42)

  humanos = maquinas + 1 #siempre hay un humano mas que cantidad de maquinas
  t = T * p.hora
  t_turno = p.turno * p.hora
  tiempo_manipulacion_h = np.random.normal(p.mu, p.sigma)
  ciclo_humano = p.ciclo_maquina + tiempo_manipulacion_h

  sum_inversas = 0

  for i in range(humanos):
    sum_inversas = sum_inversas + 1/p.MTBFh
  MTBF_humano_total = 1/sum_inversas


  sum_inversas = 0
  for i in range(maquinas):
    sum_inversas = sum_inversas + 1/p.MTBFm
  MTBF_maquina_total = 1/sum_inversas


  fallas_h = np.random.poisson(t/MTBF_humano_total)
  fallas_m = np.random.poisson(t/MTBF_maquina_total)


  tiempo_produccion = (t - int(t / t_turno) * (p.t_preparacion + p.descanso)
                       - p.MTTRh * fallas_h
                       - p.MTTRm * fallas_m)


  P = int(tiempo_produccion / ciclo_humano)


  calidad = np.random.uniform(0, 1, P)
  estado = calidad < p.Pbh

  Pb = np.sum(estado)
  Pd = P - Pb

  max_limit = t / p.ciclo_maquina
  oee = Pb / max_limit

  return fallas_h, fallas_m, P, Pb, Pd, oee