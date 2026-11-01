# Unidades (todo en segundos)
minuto = 60
hora = 3600
turno = 8 * hora

# Compartidos
t_preparacion = 15 * minuto
ciclo_maquina = 5

# Humano
mu = 10
sigma = 2
descanso = 15 * minuto
MTBFh = 8 * hora
MTTRh = 5 * minuto
Pbh = 0.9973

# Máquina
MTBFm = 500 * hora
MTTRm = 4 * hora


MTBFmm = 1000 * hora

# Robot
tiempo_manipulacion = 1
MTBFr = 1000 * hora
MTTRr = 4 * hora
Pbr = 0.99999