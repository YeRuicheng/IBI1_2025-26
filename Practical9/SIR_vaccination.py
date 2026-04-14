import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#beta: the Pr that S becomes I per contact with an infected person
#gammma: the Pr that I becomes R per time point
beta = 0.3
gamma = 0.05
N = 10000
I0 = 1
R0 = 0
time_points = 1000
vaccine_rate = np.arange(0, 1.1, 0.1)



for index, v in enumerate(vaccine_rate):
    V0 = int(N * v)
    S0 = max(N - V0 - I0 - R0, 0)

    S = [S0]
    I = [I0]
    R = [R0]

    for t in range(time_points):
        Pr_I = beta*I[-1]/N
        new_infections = np.random.choice(range(2), S[-1], p=[1-Pr_I, Pr_I]).sum()
        new_recovered = np.random.choice(range(2), I[-1], p=[1-gamma, gamma]).sum()

        S_new = S[-1] - new_infections
        I_new = I[-1] + new_infections - new_recovered
        R_new = R[-1] + new_recovered

        S.append(S_new)
        I.append(I_new)
        R.append(R_new)

    plt.plot(I, color = cm.viridis(30), label=f'{int(v*100)}%')

plt.title('SIR Model with Different Vaccination Rates')
plt.xlabel('Time')
plt.ylabel('Number of Infected people')
plt.legend()
plt.show()