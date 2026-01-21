import random
import numpy as np
import matplotlib.pyplot as plt
history = []
sims = int(input('Enter number of rolls: '))
i = 0
rolls_array = np.random.randint(1,7,size=sims)
#print(history)
faces, count = np.unique(rolls_array, return_counts=True)
print(faces,count)
plt.bar(faces, count, color='green', edgecolor='black')
plt.show()

