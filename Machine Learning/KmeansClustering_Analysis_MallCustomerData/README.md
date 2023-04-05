# Clustering Analysis of Mall Customer Data

This repository contains code for performing clustering analysis on Mall Customer data using the KMeans algorithm. The code is written in Python and utilizes popular data science libraries such as pandas, matplotlib, seaborn, and scikit-learn.

## Getting Started

### Dataset

The dataset used in this analysis is called 'Mall_Customers.csv' and it contains information about customers of a mall. The dataset has the following columns:

CustomerID: A unique identifier for each customer.

Age: Age of the customer.

Annual Income (k$): Annual income of the customer in thousands of dollars.

Spending Score (1-100): A score that represents the customer's spending behavior in the mall, ranging from 1 (low spending) to 100 (high spending).

### Code Overview
The code performs the following steps:

Importing necessary libraries: The required libraries for data preprocessing, visualization, and clustering are imported, including pandas, matplotlib, seaborn, and scikit-learn.

Loading the dataset: The 'Mall_Customers.csv' dataset is loaded into a pandas DataFrame object called 'dataset'.

Data exploration: Basic information about the dataset, such as its shape, first few rows, and descriptive statistics, are printed to gain an initial understanding of the data.

Data preprocessing: Relevant variables for clustering, which include 'CustomerID', 'Age', 'Annual Income (k$)', and 'Spending Score (1-100)', are selected and stored in a new DataFrame called 'dataset_1'. The irrelevant variables are dropped from the dataset.

Data visualization: The relationship between 'Annual Income' and 'Spending Score' is visualized using a scatter plot created with seaborn and matplotlib.

KMeans clustering: A KMeans clustering model with 5 clusters is created using scikit-learn's KMeans class. The model is trained on the 'dataset_1' data.

Determining the optimal number of clusters: The within-cluster sum of squares (WSS) is calculated for different values of k (number of clusters) to determine the optimal value of k. The silhouette score, which measures the compactness and separation of clusters, is also calculated.

Visualization of results: The WSS values are plotted against the number of clusters to create an elbow plot, which helps in identifying the optimal number of clusters. The 'dataset_1' data is then plotted with different colors assigned to each cluster, and the cluster centers are also plotted.

Conclusion: Based on the analysis, the optimal number of clusters is determined to be 5. The final clustering results are visualized using scatter plots and cluster center plots.

### Dependencies
The following Python libraries are required to run the code:

pandas
matplotlib
seaborn
numpy
scikit-learn

Credits
This code is developed by Josefina as part of a data analysis project. The 'Mall_Customers.csv' dataset is obtained from course BAN230 Applied data mining and modelling
