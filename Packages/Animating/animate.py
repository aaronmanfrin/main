import random

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x_values= [ ]
y_values= [ ]

for _ in range(100): ## the _ is aghost variable meaning the val wont show up inthe loop

    x_values.append(random.randint(0,100)) ## random nums to plot
    y_values.append(random.randint(0,100))

    plt.xlim(0,100) #limit to graph
    plt.ylim(0,100)

    plt.scatter(x_values, y_values, color = 'black'), # scattering values
    plt.pause(0.0001) ## pausing between each plot


plt.show()
 ### section 2

x_values= [ ]
y_values= [ ]

for i in range(100): ## the _ is aghost variable meaning the val wont show up inthe loop

    x_values.append(random.randint(0,100)) ## random nums to plot
    y_values.append(random.randint(0,100))

    if i % 5 == 0: ## so we dont plot so mamy points
        plt.xlim(0,100) #limit to graph
        plt.ylim(0,100)

        plt.scatter(x_values, y_values, color = 'black'), # scattering values
        plt.pause(0.0001) ## pausing between each plot


plt.show()


### section 3

x_values= [ ]
y_values= [ ]

reg = LinearRegression()
for i in range(100): ## the _ is aghost variable meaning the val wont show up inthe loop
    plt.clf()## clearing plot after each point
    x_values.append(random.randint(0,100)) ## random nums to plot
    y_values.append(random.randint(0,100))

    x = np.array(x_values) ## changing list to numpy array
    x=x.reshape(-1,1) ## reshaping list

    y=np.array(y_values)
    y=y.reshape(-1,1)

    if i % 5 == 0: ## so we dont plot so mamy points
        reg.fit(x,y) ## creating reg line for x and y
        plt.xlim(0,100) #limit to graph
        plt.ylim(0,100)
        plt.plot(list(range(100)),reg.predict(np.array([x for x in range(100)]).reshape(-1,1))) ## plotting our regline

        plt.scatter(x_values, y_values, color = 'black'), # scattering values
        plt.pause(0.0001) ## pausing between each plot


plt.show()