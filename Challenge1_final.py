


import pandas as pd
from statistics import stdev
import seaborn as sns

# The first step is to load in the dataset

df_path = "/Users/ishanisootha/Desktop/Shopify/2019 Winter Data Science Intern Challenge Data Set.xls"
df = pd.read_excel(df_path) # Reading Data Set


# Since every erroneous duplicate will automatically be assigned 
# a unique order id (assumption), we drop this column before finding 
# duplicate entries

del df['order_id']

# A precautionary measure to clean dataset, and remove duplicate entries
df.drop_duplicates()


# Inserts a new column that calculates mean cost per sneaker per order
df['cost_of_sneaker'] = df['order_amount']/df['total_items']


# print(df['cost_of_sneaker'].median())     # For (c)


# Calculates the IQR for the cost per sneaker, to find outliers in data
# which can arise due to erroneous entries and abnormal behaviour

Q1 = df['cost_of_sneaker'].quantile(0.25)   # Calculates 25th percentile
Q3 = df['cost_of_sneaker'].quantile(0.75)   # Calculates 75th percentile
IQR = Q3 - Q1                               # Calculates IQR

# sns.boxplot(x=df['cost_of_sneaker'])  # Visual representation of outliers

# Outliers are removed from the data set

df_final = df[~((df['cost_of_sneaker']<(Q1 - 1.5*IQR)) | 
                (df['cost_of_sneaker']>(Q3 + 1.5*IQR)))]

# Required Average Order Value is Calculated 

Average_Order_Value = df_final['order_amount'].mean()

# print(Average_Order_Value)

# print(df_final['cost_of_sneaker'].median())     # For (c)

 
