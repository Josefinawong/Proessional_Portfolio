#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing preprocessing libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importing dataset
dataset = pd.read_csv('Mall_Customers.csv')

# Basic information about dataset
print(dataset.shape)
print(dataset.head())
print(dataset.describe())


# In[19]:


# Select the relevant variables for clustering
relevant_vars = ['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# Drop the irrelevant variables
dataset_1 = dataset[relevant_vars]


print(dataset_1.head())


# In[87]:


sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=dataset)
plt.show()


# In[88]:


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# In[89]:


# Creating an instance of KMeans
k_means = KMeans(n_clusters=5)


# In[90]:


k_means.fit(dataset_1)


# In[91]:


# Predicting the clusters
y_pred = k_means.predict(dataset_1)


# In[92]:


# Calculating the WSS
# Calculate WSS for each value of k
wss = []
for k in range(1, 10):
    k_means = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
    k_means.fit(dataset_1)
    wss.append(k_means.inertia_)


# In[93]:


# Calculating the Silhouette Score
silhouette = silhouette_score(dataset_1, y_pred)


# In[94]:


# Printing the WSS and Silhouette Score
print("WSS:", wss)
print("Silhouette Score:", silhouette)


# In[95]:


# Plot the values of K vs WSS
import matplotlib.pyplot as plt
plt.plot(range(1,10), wss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WSS')
plt.show()


# In[99]:


# fit the model with the optimal k value
optimal_k = 5

kmeans = KMeans(n_clusters=optimal_k)
kmeans.fit(dataset_1)


# In[100]:


# Instantiate a KMeans model with the optimal K value
model = KMeans(n_clusters=optimal_k)
model.fit(dataset_1)

# Get the cluster labels for each data point
labels = model.predict(dataset_1)


# In[101]:


# Create a scatter plot of the data points with colors assigned by cluster
plt.scatter(dataset_1.iloc[:, -1], dataset_1.iloc[:, -2], c=labels, cmap='rainbow')
plt.show()


# In[102]:


# plot the centers of the clusters with a larger size
plt.scatter(kmeans.cluster_centers_[:, -1], kmeans.cluster_centers_[:, -2], s=100, color='black')
plt.show()


# In[103]:


centers = kmeans.cluster_centers_
plt.scatter(centers[:, -1], centers[:, -2], c='red', s=200, alpha=0.5)
plt.show()


# In[ ]:




