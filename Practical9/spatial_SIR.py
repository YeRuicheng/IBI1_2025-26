import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
time_steps = 100

# 0 for Susceptible, 1 for Infected, 2 for Recovered

# make array of all susceptible population
population = np.zeros( (100, 100) )

outbreak = np.random.choice(range(100) ,2)
population [outbreak [0] , outbreak [1]] = 1

plt.figure(figsize =(6,4),dpi=150)
plt.imshow(population , cmap='viridis', interpolation='nearest')

for step in range(time_steps):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # recover with probability gamma
        if np.random.choice(range(2),1,p=[1-gamma,gamma])[0]==1:
            population[x,y]=2
        else:
            # infect each neighbour with probability beta
            # infect all 8 neighbours (this is a bit finicky, is there a better way?):
            for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    # don't infect yourself! (Is this strictly necessary?)
                    if (xNeighbour,yNeighbour) != (x,y):
                        # make sure I don't fall off an edge
                        if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                            # only infect neighbours that are not already infected!
                            if population[xNeighbour,yNeighbour]==0:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

    recover = np.random.choice(range(2), 1, p=[1-gamma, gamma])[0]
    if recover == 1:
            population[x, y] = 2
    
    if (step + 1) % 20 == 0:
        plt.clf()
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step+1}')
        plt.pause(0.2)
plt.show()