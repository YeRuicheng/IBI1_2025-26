import numpy as np
import matplotlib.pyplot as plt

# Model parameters definition
# beta: the Pr that S becomes I per contact with an infected person
beta = 0.3
# gamma: the Pr that I becomes R per time point
gamma = 0.05

# Total population size
N = 10000
# Initial number of infected individuals
I0 = 1
# Initial number of susceptible individuals
S0 = 9999
# Initial number of recovered individuals
R0 = 0

# Total simulation time steps
time_points = 1000

# Initialize lists to store S, I, R values over time
S = [S0]
I = [I0]
R = [R0]

for t in range(time_points):
    # Calculate probability of infection for susceptible individuals
    Pr_I = beta*I[-1]/N
    new_infections = np.random.choice(range(2), S[-1], p=[1-Pr_I, Pr_I]).sum()
    new_recovered = np.random.choice(range(2), I[-1], p=[1-gamma, gamma]).sum()

    # Update population counts for next time step
    S_new = S[-1] - new_infections
    I_new = I[-1] + new_infections - new_recovered
    R_new = R[-1] + new_recovered

    # Append updated values to the lists
    S.append(S_new)
    I.append(I_new)
    R.append(R_new)

# Create a plot of the SIR model results
plt.figure(figsize =(6,4), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()

# Save the plot as a .png file, and then display it
plt.savefig('SIR.png')
plt.show()