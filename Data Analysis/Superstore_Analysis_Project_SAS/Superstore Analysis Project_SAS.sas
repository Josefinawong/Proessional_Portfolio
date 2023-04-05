/***********************************************
* Superstore Analysis Project
***********************************************/

/* Import Orders data */
proc import out = Orders
datafile='/home/u62273481/ban110/Superstore(1).xlsx'
out=Orders dbms=xlsx;
getnames=Yes;
sheet="Orders";
run;

/* Import Returns data */
proc import out = Returns
datafile='/home/u62273481/ban110/Superstore(1).xlsx'
out=Returns dbms=xlsx;
getnames=Yes;
sheet="Returns";
run;

/* Sort Orders and Returns data */
proc sort data=orders out=sorted_orders;
by 'order ID'n;
run;

proc sort data=returns out=sorted_returns;
by 'order ID'n;
run;

data order_returned;
merge sorted_orders(IN=inorders) sorted_returns(IN=inreturns);
by 'order ID'n;
if Inorder=1 and Inreturns=1;
run;

proc sort data=orders out=sorted_order;
by 'order ID'n;
run;
proc sort data=returns out=sorted_returns;
by 'order ID'n;
run;

/* Merge Orders and Returns data to identify returned orders */
data Orders_Returned;
merge sorted_order(IN=Inorder) sorted_returns(IN=Inreturns);
by 'Order ID'n;
if Inorder=1 and Inreturns=1;

label 'order date'n = "Order_date"
      'customer name'n = "Customer_name"
      'Postal_code'n = "Postal_Code"
      'Product Name'n = "Product_Name";
run;

/* Print the first 10 rows of Orders_Returned data */
proc print data=orders_returned (obs=10) label;
var 'order date'n 'customer name'n city 'Postal Code'n 'Product Name'n Sales quantity ;
run;

*Creating a summary report by product category;
proc summary data=Orders_Returned nway;
  class Category;
  var Sales Quantity Profit;
  output out=Summary_Report
    sum(Sales)=Total_Sales
    sum(Quantity)=Total_Quantity
    sum(Profit)=Total_Profit;
run;

proc print data=Summary_Report noobs;
  var Category Total_Sales Total_Quantity Total_Profit;
  label Total_Sales = "Total Sales"
        Total_Quantity = "Total Quantity"
        Total_Profit = "Total Profit";
run;

*Generate a bar chart to visualize sales by product category;
proc sgplot data=Summary_Report;
  vbar Category / response=Total_Sales
                 stat=sum
                 group=Category
                 dataskin=pressed;
  xaxis display=(nolabel);
  yaxis grid;
  title "Total Sales by Product Category";
run;

