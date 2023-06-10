import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
population_size = 10000
initial_infected = 10
infection_rate = 0.3
recovery_rate = 0.1
simulation_days = 100

# Initialize arrays
susceptible = np.zeros(simulation_days)
infected = np.zeros(simulation_days)
recovered = np.zeros(simulation_days)

# Set initial conditions
susceptible[0] = population_size - initial_infected
infected[0] = initial_infected

# Perform simulation
for day in range(1, simulation_days):
    new_infections = infection_rate * \
        susceptible[day - 1] * infected[day - 1] / population_size
    new_recoveries = recovery_rate * infected[day - 1]

    susceptible[day] = susceptible[day - 1] - new_infections
    infected[day] = infected[day - 1] + new_infections - new_recoveries
    recovered[day] = recovered[day - 1] + new_recoveries

# Create animated graph
fig, ax = plt.subplots()
ax.set_xlim(0, simulation_days)
ax.set_ylim(0, population_size)
ax.set_xlabel('Days')
ax.set_ylabel('Population')

susceptible_line, = ax.plot([], [], label='Susceptible')
infected_line, = ax.plot([], [], label='Infected')
recovered_line, = ax.plot([], [], label='Recovered')
ax.legend()


def update_graph(day):
    susceptible_line.set_data(range(day), susceptible[:day])
    infected_line.set_data(range(day), infected[:day])
    recovered_line.set_data(range(day), recovered[:day])

    return susceptible_line, infected_line, recovered_line


ani = animation.FuncAnimation(
    fig, update_graph, frames=simulation_days, blit=True)

# Save animation as a GIF file
ani.save('population_dynamics_simulation.gif', writer='pillow')

plt.show()
