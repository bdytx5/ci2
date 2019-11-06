import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target












plt.figure(2, figsize=(8, 6))
plt.clf()

ws = X[:, :1]
hs = X[:, 1:2]
tws = np.ones(50)
ones = np.ones(50)
zrs = np.zeros(50)


data = ([ws[0:50],hs[0:50]], [ws[50:100],hs[50:100]], [ws[100:150],hs[100:150]])
colors = ("red", "green", "blue")
groups = ("1", "2", "3")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor='#E6E6E6')

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()


# Plot the training points


# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
# fig = plt.figure(1, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
# X_reduced = PCA(n_components=3).fit_transform(iris.data)
# ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
#            cmap=plt.cm.Set1, edgecolor='k', s=40)
# ax.set_title("First three PCA directions")
# ax.set_xlabel("1st eigenvector")
# ax.w_xaxis.set_ticklabels([])
# ax.set_ylabel("2nd eigenvector")
# ax.w_yaxis.set_ticklabels([])
# ax.set_zlabel("3rd eigenvector")
# ax.w_zaxis.set_ticklabels([])

