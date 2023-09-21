import numpy as np
import matplotlib.pyplot as plt
import sympy
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Circle

# Pendulum Parameters:
m = 1  # kg
g = 9.8  # m/s^2
l = 1  # m

# Create Symbols for Time:
t = sympy.Symbol('t')  # Creates symbolic variable t

# Create Generalized Coordinates as a function of time: q = [theta]
th = sympy.Function('th')(t)
# Creates a symbolic function with respects to the symbolic variable t

# Position Equation: r = [x, y]
r = np.array([l * sympy.sin(th), -l * sympy.cos(th)])  # Position of pendulum 
# (Note you must use SymPy's math functions when using symbolic variables)
# Here is to demonstrate that you can build numpy arrays that contain symbolic variables
# This is useful for more complex systems
# You could have easily formulated this as:
# x = l * sympy.sin(th)
# y = -l * sympy.cos(th)

# Velocity Equation: d/dt(r) = [dx/dt, dy/dt]
v = np.array([r[0].diff(t), r[1].diff(t)])  # Velocity of pendulum
# To take a derivative of an expression you can call diff as a method using the "." operator 
# Syntax: expr.diff(x), where expr is your expression containing symbolic variables 
# and x is the variable you want the derivative to be respects to
# Again, you could have easily formulated this as:
# dx = x.diff(t)
# dy = y.diff(t)

# Energy Equations:
T = 1/2 * m * np.dot(v, v)  # Kinetic Energy
V = m * g * r[1]  # Potential Energy
L = T - V  # Lagrangian

# Lagrange Terms:
dL_dth = L.diff(th)
dL_dth_dt = L.diff(th.diff(t)).diff(t)
# We can take many derivatives at once:
# expr.diff(x).diff(y) == d/dy[ d/dx(expr)]

# Euler-Lagrange Equations: dL/dq - d/dt(dL/ddq) = 0
th_eqn = dL_dth - dL_dth_dt

# Replace Time Derivatives and Functions with Symbolic Variables:
replacements = [(th.diff(t).diff(t), sympy.Symbol('ddth')), (th.diff(t), sympy.Symbol('dth')), (th, sympy.Symbol('th'))]
# Note: Replace in order of decreasing derivative order
th_eqn = th_eqn.subs(replacements)  # Use Subs method to substitute in the Symbolic Variables

th_eqn = sympy.simplify(th_eqn)

# Solve for ddth:
ddth_eqn = sympy.solvers.solve(th_eqn, sympy.Symbol('ddth'))  # Solves for ddth
# Syntax: sympy.solvers.solve(expr, x) where expr is your expression 
# and x is the symbolic variable you want to solve for

ddth_eqn = ddth_eqn[0]  # We need to do this to avoid issues with the next part

# Generate Lambda Function for ddth_eqn:
function_input = (sympy.Symbol('th'), sympy.Symbol('dth')) # These are the ordered inputs to the generated lambda function
ddth_eqn = sympy.utilities.lambdify(function_input, ddth_eqn, "numpy")  # Generates a Lambda Function using the numpy library

# Simulate System:
x0 = np.pi/4, 0  # x0 = [th, dth]
dt = 0.001
sim_time = 10
time = np.arange(0, sim_time, dt)
sim_length = len(time)

# Initialize Arrays:
th_vec = np.zeros(sim_length)
dth_vec = np.zeros(sim_length)
x_vec = np.zeros(sim_length)
y_vec = np.zeros(sim_length)

# Evaluate Initial Conditions:
th_vec[0] = x0[0]
dth_vec[0] = x0[1]
x_vec[0] = l * np.sin(th_vec[0])
y_vec[0] = -l * np.cos(th_vec[0])

# Euler Integration:
for i in range(1, sim_length):
    # Evauluate ddth:
    ddth = ddth_eqn(th_vec[i-1], dth_vec[i-1])
    # Euler Step Integration:
    th_vec[i] = th_vec[i-1] + dth_vec[i-1]*dt
    dth_vec[i] = dth_vec[i-1] + ddth*dt
    # Animation States:
    x_vec[i] = l * np.sin(th_vec[i])
    y_vec[i] = -l * np.cos(th_vec[i])

    # Setup Figure: Initialize Figure / Axe Handles
fig, ax = plt.subplots()
p, = ax.plot([], [], color='cornflowerblue')
ax.axis('equal')
ax.set_xlim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Pendulum Simulation:')
video_title = "simulation"

# Initialize Patch:
c = Circle((0, 0), radius=0.1, color='cornflowerblue')
ax.add_patch(c)

# Setup Animation Writer:
FPS = 20
sample_rate = int(1 / (dt * FPS))
dpi = 300
writerObj = FFMpegWriter(fps=FPS)

# Draw Pin Joint:
pin_joint = Circle((0, 0), radius=0.025, color='black', zorder=10)
ax.add_patch(pin_joint)

# Plot and Create Animation:
with writerObj.saving(fig, f"{video_title}.mp4", dpi):
    for i in range(0, sim_length, sample_rate):
        # Update Pendulum Arm:
        x_data_points = [0, x_vec[i]]
        y_data_points = [0, y_vec[i]]
        p.set_data(x_data_points, y_data_points)
        # Update Pendulum Patch:
        patch_center = x_vec[i], y_vec[i]
        c.center = patch_center
        # Update Drawing:
        fig.canvas.draw()  # Update the figure with the new changes
        # Grab and Save Frame:
        writerObj.grab_frame()

