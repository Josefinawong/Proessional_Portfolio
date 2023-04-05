# Superstore Analysis Project

This project involves analyzing sales data from the Superstore dataset, which includes information about customer orders and returns. The goal of this project is to gain insights into customer behavior and identify any patterns or trends in returned orders.

## Data Import and Preparation

The project starts with importing the Orders and Returns data from an Excel file using SAS PROC IMPORT. The data is sorted by 'Order ID' using PROC SORT, and then merged to create a new dataset 'Orders_Returned' that identifies returned orders.

## Data Analysis

The 'Orders_Returned' dataset is then analyzed to generate summary statistics using PROC SUMMARY. The summary statistics include total sales, total quantity, and total profit, grouped by product category. The results are stored in a new dataset 'Summary_Report'.

A bar chart is generated using PROC SGPLOT to visualize the total sales by product category, providing a visual representation of the sales performance of different product categories.

## Results

The results of the analysis are printed using PROC PRINT, displaying the 'Orders_Returned' dataset with labeled variables. Additionally, the 'Summary_Report' dataset is printed to display the summary statistics of sales, quantity, and profit by product category.

## Conclusion

Based on the analysis of the Superstore dataset, it can be concluded that certain product categories have higher returns, and further investigation may be needed to identify the reasons for these returns. The bar chart provides a visual representation of the sales performance by product category, which can help in making informed business decisions.


