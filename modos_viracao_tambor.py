import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros

m = 1 #modo angular  
n = 2 #modo radial
a = 1 #raio do tambor

raizes_j = jn_zeros(m,n)
x_mn = raizes_j[0]
k_mn = x_mn/a

#Grid

#criando um vetor 1D para o raio r, de 0 até a
r_vec = np.linspace(0, a, 50)
#ciando um vetor 1D para o angulo theta, 0 até 2pi
theta_vec = np.linspace(0, 2*np.pi, 100)

#transformando os vetores em duas matrizes 2D para plotarmos o gráfico 3D
R, THETA = np.meshgrid(r_vec, theta_vec)

#solução
U = jn(m, k_mn*R)*np.cos(m*THETA) #camplitude do tambor, para cada ponto
#para 3d, trocamos as coordenadas para a leitura no matplotlib
X = R*np.cos(THETA)
Y = R*np.sin(THETA)

#plotagem:
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X, Y, U)
ax.set_title(f"Modos de Vibração numa Membrana Circular\nModo (m={m}, n={n})")
plt.show()