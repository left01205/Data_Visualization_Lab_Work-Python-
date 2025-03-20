#Scatterplot

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

iris = datasets.load_iris()
sepal_length = iris.data [:,0]
sepal_width = iris.data [:,1]

species = iris.target

sns.set_style("whitegrid")

plt.figure(figsize=(8,5))


sns.scatterplot(x=sepal_length,y=sepal_width,hue=species,palette="bright")

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter plot of Sepal Length vs Sepal Width')

plt.show()
