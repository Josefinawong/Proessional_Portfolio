# Customer Segmentation Analysis

This repository contains code for performing customer segmentation analysis on a mall customer dataset. The goal of the analysis is to identify distinct customer segments based on their age, annual income, and spending score.

## Dataset

The analysis uses the "Mall_Customers.csv" dataset, which contains information about mall customers. The dataset includes the following variables:

- CustomerID: Unique identifier for each customer
- Age: Age of the customer
- Annual Income (k$): Annual income of the customer in thousands of dollars
- Spending Score (1-100): Score reflecting the customer's spending behavior

## Analysis Steps

1. Importing the necessary libraries, including pandas, matplotlib, seaborn, and numpy.
2. Importing the dataset using `pd.read_csv()` function.
3. Exploring the basic information about the dataset using `shape`, `head()`, and `describe()` functions.
4. Selecting the relevant variables for clustering and dropping the irrelevant variables.
5. Visualizing the relationship between the annual income and spending score using a scatter plot.
6. Performing K-means clustering using the `KMeans` algorithm from the scikit-learn library.
7. Calculating the within-cluster sum of squares (WSS) and silhouette score to determine the optimal number of clusters.
8. Plotting the WSS against the number of clusters to identify the optimal number of clusters using the elbow method.
9. Fitting the K-means model with the optimal number of clusters.
10. Creating a scatter plot of the data points with colors assigned by cluster and visualizing the cluster centers.
11. Analyzing the characteristics of each customer segment, including the number of customers, mean values of variables, and distribution of variables using box plots.

## Results

The analysis identifies distinct customer segments based on their age, annual income, and spending score. 
The number of clusters is determined to be 5 using the elbow method. Each cluster represents a different customer segment with specific characteristics. The analysis provides insights into the number of customers in each cluster, the mean values of variables for each cluster, and the distribution of variables within each cluster.
