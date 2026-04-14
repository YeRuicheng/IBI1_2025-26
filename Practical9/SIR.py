import numpy as np
import matplotlib . pyplot as plt

#beta: the Pr that S becomes I per contact with an infected person
#gammma: the Pr that I becomes R per time point
beta = 0.3
gamma = 0.05
N = 10000
I0 = 1
S0 = 9999
R0 = 0
time_points = 1000

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

plt.figure(figsize =(6,4), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('C:/Users/叶睿城/Desktop/SIR.png')
plt.show()