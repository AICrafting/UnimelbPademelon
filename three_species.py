import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lotka_volterra(t, z, alpha, beta1, beta2, lambda1, omega1, lambda2, omega2):
    x, y, z = z
    dxdt = alpha * x - beta1 * x * y - beta2 * x * z
    dydt = -lambda1 * y + omega1 * x * y
    dzdt = -lambda2 * z + omega2 * x * z
    return [dxdt, dydt, dzdt]

alpha = 0.15
beta1 = 0.003
beta2 = 0.002  # Predation rate of red foxes on pademelons
lambda1 = 0.18
omega1 = 0.0016
lambda2 = 0.2  # Natural death rate of red foxes
omega2 = 0.001786  # Growth rate of red foxes due to predation on pademelons

x0 = 180
y0 = 30
z0 = 10  # Initial population of red foxes
initial_conditions = [x0, y0, z0]

t_span = (0, 200)
t_eval = np.linspace(*t_span, 1000)

solution = solve_ivp(lotka_volterra, t_span, initial_conditions, args=(alpha, beta1, beta2, lambda1, omega1, lambda2, omega2), t_eval=t_eval)

plt.figure(figsize=(12, 8))
plt.plot(solution.t, solution.y[0], label='Pademelons (x)')
plt.plot(solution.t, solution.y[1], label='Thylacines (y)')
plt.plot(solution.t, solution.y[2], label='Red Foxes (z)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Three-Species Lotka-Volterra Model')
plt.grid()
plt.show()