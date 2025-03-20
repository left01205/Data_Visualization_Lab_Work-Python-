#Q-Q
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

np.random.seed(0)
data = np.random.random(1000)

stats.probplot(data, dist = 'norm',plot=plt)
plt.title('Q-Q Plot')
plt.xlabel ('Theoritical Quantile')
plt.ylabel('Sample Quantile')
plt.grid()
plt.show()
