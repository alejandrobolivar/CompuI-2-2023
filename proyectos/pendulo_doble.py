g = 9.82
L = 0.5
m = 0.1

def dx(x, t):
    """
    El lado derecho de la EDO del péndulo
    """
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    
    dx1 = 6.0/(m*L**2) * (2 * x3 - 3 * np.cos(x1-x2) * x4)/(16 - 9 * np.cos(x1-x2)**2)
    dx2 = 6.0/(m*L**2) * (8 * x4 - 3 * np.cos(x1-x2) * x3)/(16 - 9 * np.cos(x1-x2)**2)
    dx3 = -0.5 * m * L**2 * ( dx1 * dx2 * np.sin(x1-x2) + 3 * (g/L) * np.sin(x1))
    dx4 = -0.5 * m * L**2 * (-dx1 * dx2 * np.sin(x1-x2) + (g/L) * np.sin(x2))
    
    return [dx1, dx2, dx3, dx4]

# define la condición inicial
x0 = [np.pi/4, np.pi/2, 0, 0]

# tiempos en los que se resolverá la EDO: desde 0 hasta 10 segundos
t = np.linspace(0, 10, 250)

# resuelve el sistema de EDOs
x = odeint(dx, x0, t)

# grafica los ángulos como funciones del tiempo

fig, axes = plt.subplots(1,2, figsize=(12,4))
axes[0].plot(t, x[:, 0], 'r', label="theta1")
axes[0].plot(t, x[:, 1], 'b', label="theta2")


x1 = + L * np.sin(x[:, 0])
y1 = - L * np.cos(x[:, 0])

x2 = x1 + L * np.sin(x[:, 1])
y2 = y1 - L * np.cos(x[:, 1])
    
axes[1].plot(x1, y1, 'r', label="pendulo1")
axes[1].plot(x2, y2, 'b', label="pendulo2")
axes[1].set_ylim([-1, 0])
axes[1].set_xlim([1, -1]);
