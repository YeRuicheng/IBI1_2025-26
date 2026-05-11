import numpy as np
import matplotlib.pyplot as plt

# Model parameters:
# Infection probability
beta = 0.3
# Recovery probability    
gamma = 0.05
# Total simulation time steps
time_steps = 100

# 0 for Susceptible, 1 for Infected, 2 for Recovered

# make array of all susceptible population
population = np.zeros( (100, 100) )

# Randomly select one point for initial outbreak
outbreak = np.random.choice(range(100) ,2)
# Set the initial outbreak point to infected (1)
population [outbreak [0] , outbreak [1]] = 1

# Initialize plot for visualization
plt.figure(figsize =(6,4),dpi=150)
plt.imshow(population , cmap='viridis', interpolation='nearest')
plt.title("Time 0")
plt.pause(0.5) # Short pause to display initial state

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
    
    # Update the plot every 20 steps for visualization
    if (step + 1) % 20 == 0:
        plt.clf() # Clear the current figure to update with new data
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step+1}')
        plt.pause(0.5) # Short pause to display update

# Show the final state (time 100) of the population after the simulation
plt.show()