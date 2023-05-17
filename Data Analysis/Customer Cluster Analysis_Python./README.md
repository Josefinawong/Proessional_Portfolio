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

## Impact on business decision-making
1. Targeted Marketing Strategies: By identifying distinct customer segments based on age, annual income, and spending score, businesses can tailor their marketing strategies to better meet the needs and preferences of each segment. This can involve developing targeted advertising campaigns, personalized offers, and product recommendations that resonate with the characteristics and behaviors of each segment. The analysis enables businesses to allocate their marketing resources more effectively and increase the effectiveness of their promotional efforts.

2. Product Development and Customization: Understanding customer segments can provide insights into the specific preferences and requirements of different groups of customers. Businesses can leverage this information to develop new products or customize existing ones to better serve each segment's needs. By aligning product features, pricing, and messaging with the characteristics of different segments, businesses can enhance customer satisfaction, loyalty, and retention.

3. Customer Experience Enhancement: Customer segmentation analysis can help businesses identify opportunities for improving the overall customer experience. By gaining insights into the unique characteristics and behaviors of different customer segments, businesses can optimize various touchpoints along the customer journey. This includes enhancing website design, optimizing in-store layouts, improving customer service, and personalizing interactions to create tailored experiences that resonate with each segment.

4. Resource Allocation and ROI Optimization: By understanding the size and value of each customer segment, businesses can allocate their resources effectively. This includes optimizing inventory management, staffing levels, and operational processes to match the specific demands and preferences of different segments. Additionally, businesses can evaluate the return on investment (ROI) of their marketing initiatives by analyzing the performance of each segment separately. This allows them to focus their efforts and resources on the segments that yield the highest ROI.
