# import packages
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# generate data
# n== number of trials,p== probability of each trial
n, p = 10, .6
data = np.random.binomial(n, p, 10000)

# plotting a histogram
ax = sns.distplot(data,
                  bins=20,
                  kde=False,
                  color='red',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')

plt.show()
