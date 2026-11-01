import numpy as np
import parametros as p
import modelo1 as m1

def Modelo_robots(T, maquinas):

  robots = maquinas + 1 #siempre hay un robot mas que cantidad de maquinas

  t = T * p.hora

  t_turno = p.turno * p.hora
  ciclo_robot = p.ciclo_maquina + p.tiempo_manipulacion

  sum_inversas = 0

  for i in range(robots):
    sum_inversas = sum_inversas + 1/p.MTBFr

  MTBF_robot_total = 1/sum_inversas


  sum_inversas = 0

  for i in range(maquinas):
    sum_inversas = sum_inversas + 1/p.MTBFm

  MTBF_maquina_total = 1/sum_inversas



  fallas_r = np.random.poisson(t/MTBF_robot_total)
  fallas_m = np.random.poisson(t/MTBF_maquina_total)

  t_reparacion_r = p.MTTRr
  t_reparacion_m = p.MTTRm

  tiempo_produccion = (t - int(t / t_turno) * p.t_preparacion
                      - t_reparacion_r * fallas_r
                      - t_reparacion_m * fallas_m)


  P = int(tiempo_produccion / ciclo_robot)  # piezas producidas

  calidad = np.random.uniform(0, 1, P)

  estado = calidad < p.Pbr

  Pb = np.sum(estado)   # piezas buenas
  Pd = P - Pb

  max_limit = m1.Modelo_ideal(t)
  oee = Pb / max_limit

  return fallas_r, fallas_m, P, Pb, Pd, oee