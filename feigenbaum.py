import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def feigenbaum_attractor(x0, r_start, r_end, num_points):
    r_values = []
    x_values = []

    r_step = (r_end - r_start) / num_points
    r = r_start

    for _ in range(num_points):
        x = x0

        for _ in range(100):  # Discard transient
            x = r * x * (1 - x)

        for _ in range(200):  # Collect data
            x = r * x * (1 - x)
            r_values.append(r)
            x_values.append(x)

        r += r_step

    return r_values, x_values

# Generate Feigenbaum attractor
r_vals, x_vals = feigenbaum_attractor(0.5, 2.4, 4.0, 1000)

# Create the animated plot
fig, ax = plt.subplots()
scatter = ax.scatter([], [], s=0.01, color='black')
ax.set_xlim(min(r_vals), max(r_vals))
ax.set_ylim(0, 1)
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Feigenbaum Attractor')

def update(frame):
    if frame > 0:
        scatter.set_offsets(np.column_stack([r_vals[:frame], x_vals[:frame]]))
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=len(r_vals), interval=10, blit=True)

plt.show()
