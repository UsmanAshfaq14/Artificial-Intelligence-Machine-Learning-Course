# import packages
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# generate poisson data
poisson_data = np.random.poisson(lam=5, size=1000)

# plotting a histogram
ax = sns.distplot(poisson_data,
                  kde=False,
                  color='blue')
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')

plt.show()
