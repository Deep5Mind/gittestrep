# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 06:46:35 2024

@author: HP
"""

import numpy as np

import matplotlib.pyplot as plt

def g(x):
    return np.exp(np.sin(x))

def méthode_trapèzes(a, b, n):
    p = (b - a) / n
    integral = 0
    for i in range(n):
        integral += (g(a) + g(a + p)) * p / 2
        a += p
    return integral


# Définition de l'intervalle et du nombre de sous-intervalles
a = 0
b = 5
n = 100

# Calcul de l'intégrale par la méthode des trapèzes
integral_approx = méthode_trapèzes(a, b, n)
print("Approximation de l'intégrale:", integral_approx)

# Tracé des trapèzes utilisés pour l'approximation de l'intégrale
for i in range(n):
    x_trap = [a + i * (b - a) / n, a + (i + 1) * (b - a) / n]
    y_trap = [g(x_trap[0]), g(x_trap[1])]
    plt.fill_between(x_trap, y_trap, color='red', alpha=0.5)  # Utilisation de la couleur rouge pour les trapèzes

# Tracé de la fonction f(x)
x_values = np.linspace(a, b, 100)
plt.plot(x_values, g(x_values), label='g(x)')

font2 = {'family': 'Arial black', 'color': 'red', 'size': 15}
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Approximation de l\'intégrale de g(x) entre 0 et 5', loc='right', fontdict=font2)

plt.legend()
plt.grid(True)
plt.show()
print ("hello leslye you've succeded in using github , be proud girl you're on the right way")

list(enumerate(range(13)))
sum(range(5,12))
print("hi")
