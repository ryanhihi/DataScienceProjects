
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()

print(digits.DESCR)
#64 values represent the pixel colors of an image (0-16):
# 0 is white
# 16 is black
print(digits.data)

#The first data point was tagged as 0 and the last one was tagged as an 8
print(digits.target)

#Visualize the image
plt.gray()

plt.matshow(digits.images[100])

plt.show()

print(digits.target[100])

#Look at the 64 sample images:
# Figure size (width, height)

fig = plt.figure(figsize=(6, 6))

# Adjust the subplots

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images

for i in range(64):

    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position

    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value

    ax.text(0, 7, str(digits.target[i]))

plt.show()


#K-Means Clustering:
from sklearn.cluster import KMeans

#The number of k should be 10 because there should be 10 digits (0,1,2,3,4,5,6,7,8,9)
#The random_state can be any number

#create model
model = KMeans(n_clusters = 10, random_state = 42)
#fit the data
model.fit(digits.data)

#Visualize after the KMeans:
#Visualize all the centroids
fig = plt.figure(figsize = (8,3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()

#Testing
new_samples = np.array([
[0.00,0.00,0.92,2.29,1.37,0.00,0.00,0.00,0.00,0.84,7.17,7.62,7.17,0.00,0.00,0.00,0.00,1.53,7.62,5.19,7.62,1.45,0.00,0.00,0.00,0.54,4.42,4.42,7.62,1.37,0.00,0.00,0.00,0.54,4.04,7.55,5.41,0.08,0.00,0.00,0.00,5.64,7.62,7.62,7.62,7.63,2.59,0.00,0.00,1.98,3.05,3.05,3.05,3.05,0.76,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.38,0.30,0.00,0.00,0.00,0.00,0.00,0.92,6.86,5.56,0.00,0.00,0.00,0.00,0.00,4.04,7.62,6.56,0.00,0.00,0.00,0.00,0.00,2.29,5.72,7.62,0.00,0.00,0.00,0.00,0.00,0.00,3.05,7.62,0.00,0.00,0.00,0.00,0.00,3.36,7.24,7.62,5.65,0.00,0.00,0.00,0.00,2.29,4.57,4.57,4.12,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.14,6.10,6.86,6.79,1.37,0.00,0.00,0.00,5.49,7.24,4.65,5.26,0.92,0.00,0.00,0.15,7.09,5.72,2.29,2.21,0.31,0.00,0.00,0.76,7.62,7.62,7.62,7.62,6.33,0.23,0.00,0.61,7.63,7.63,7.62,7.62,7.55,0.61,0.00,0.00,3.05,3.81,3.81,3.81,1.91,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,3.36,4.57,3.81,0.08,0.00,0.00,0.00,1.15,7.62,7.24,7.62,5.11,0.00,0.00,0.00,1.52,7.62,2.06,4.42,7.62,0.00,0.00,0.00,1.45,7.62,5.95,5.72,7.62,0.00,0.00,0.00,0.00,3.20,6.33,7.17,7.62,0.00,0.00,0.00,0.92,4.58,4.57,6.25,7.62,0.00,0.00,0.00,1.37,6.10,6.10,6.10,3.51,0.00,0.00]
]
)

new_labels = model.predict(new_samples)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
