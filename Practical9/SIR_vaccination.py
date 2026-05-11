import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Model parameters
#beta: the Pr that S becomes I per contact with an infected person
beta = 0.3
#gammma: the Pr that I becomes R per time point
gamma = 0.05

# Total population size
N = 10000
# Initial number of infected individuals
I0 = 1
# Initial number of recovered individuals
R0 = 0

# Total simulation time steps
time_points = 1000

# Array of vaccination rates from 0 to 100%
vaccine_rate = np.arange(0, 1.1, 0.1)


# Loop over each vaccination rate
for index, v in enumerate(vaccine_rate):
    # Calculate initial vaccinated population
    V0 = int(N * v)
    # Calculate initial susceptible population
    S0 = max(N - V0 - I0 - R0, 0)

    # Initialize lists to store S, I, R values over time
    S = [S0]
    I = [I0]
    R = [R0]

    for t in range(time_points):
        # Infection probability for susceptible people
        Pr_I = beta*I[-1]/N
        new_infections = np.random.choice(range(2), S[-1], p=[1-Pr_I, Pr_I]).sum()
        new_recovered = np.random.choice(range(2), I[-1], p=[1-gamma, gamma]).sum()

        # Update S, I, R values for next time step
        S_new = S[-1] - new_infections
        I_new = I[-1] + new_infections - new_recovered
        R_new = R[-1] + new_recovered

        # Append updated values to the lists
        S.append(S_new)
        I.append(I_new)
        R.append(R_new)

    # Plot infected curve with color gradient based on vaccination rate
    plt.plot(I, color = cm.viridis(index / len(vaccine_rate)), label=f'{int(v*100)}%')

# Plot formatting and display
plt.title('SIR Model with Different Vaccination Rates')
plt.xlabel('Time')
plt.ylabel('Number of Infected people')
plt.legend()
plt.show()