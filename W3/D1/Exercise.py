# Exercise 1: Introduction to Data Analysis (Easy)


# Objective: Understand the basic overview and significance of data analysis.
# Task: Write a short essay or report on the following topics:

# What is data analysis?

# Data analysis is the systematic process of collecting, cleaning, transforming, and interpreting data to extract meaningful insights, identify patterns, and support decision-making.
# This process encompasses various techniques, including statistical analysis, data visualization, and predictive modeling, to convert raw data into actionable information.

# Why is data analysis important in modern contexts

# In today's data-driven world, organizations across all sectors generate vast amounts of data daily. 
# Data analysis enables these organizations to harness this data effectively, leading to informed decision-making, enhanced operational efficiency, 
# and a competitive advantage. By uncovering trends and patterns, data analysis helps businesses anticipate market shifts, understand customer behavior, 
# and optimize processes.

# List and describe three areas where data analysis is applied today.

# Healthcare: Data analysis in healthcare facilitates patient care by enabling predictive diagnostics, personalized treatment plans, and efficient resource allocation. 
# For instance, analyzing patient data can help in early disease detection and monitoring treatment effectiveness. 

# Finance: Financial institutions utilize data analysis for risk assessment, fraud detection, and customer segmentation. 
# By analyzing transaction patterns, banks can identify fraudulent activities and tailor financial products to individual customer needs. 

# Retail and E-commerce: Retailers leverage data analysis to understand consumer behavior, manage inventory, and personalize marketing strategies. 
# Analyzing purchase histories and browsing patterns allows businesses to recommend products and optimize pricing strategie



# Exercise 2: Dataset Loading and Initial Analysis

# Step 1: Set up Your Environment in Google Colab:

# # Import pandas
# import pandas as pd

# from google.colab import files
# uploaded = files.upload()

# df = pd.read_csv("your_file_name.csv")


# Display the First Few Rows

# df.head()


# Dataset Description

# df = pd.read_csv("sleep_americans.csv")
# df.head()


# df = pd.read_csv("global_mental_health.csv")
# df.head()

# df = pd.read_csv("credit_card_approvals.csv")
# df.head()



# Exercise 3

import pandas as pd

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# View data types
print(df.dtypes)

# Automatically list qualitative and quantitative columns
qualitative_columns = df.select_dtypes(include=['object']).columns.tolist()
quantitative_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

print("Qualitative Columns:", qualitative_columns)
print("Quantitative Columns:", quantitative_columns)


# Exercise 4

import pandas as pd

# Load the dataset
df = pd.read_csv("Iris.csv")  # Or use the correct path
df.head()

print(df.dtypes)


# Exercise 5

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("Iris.csv")

# Preview data
df.head()

mean = df['PetalLengthCm'].mean()
median = df['PetalLengthCm'].median()
mode = df['PetalLengthCm'].mode()[0]  # mode() returns a Series

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

plt.figure(figsize=(8, 5))
plt.hist(df['PetalLengthCm'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='PetalLengthCm')
plt.title("Boxplot of Petal Length")
plt.show()


# Findings:

# The mean petal length is approximately X cm.

# The median is slightly lower/higher than the mean, suggesting a [symmetric/slightly skewed] distribution.

# The mode indicates the most frequently occurring petal length.

# From the histogram, we observe that the majority of petals cluster around the X–Y cm range.

# The bar plot shows that Iris-virginica tends to have the longest petals, while Iris-setosa has the shortest.


# Exercise 6

import pandas as pd

# Load the dataset (update filename if needed)
df = pd.read_csv("sleep_americans.csv")

# View a preview
df.head()

# Selected Columns for Analysis:

# I selected Age Group, Gender, and Employment Status because they allow for clear group comparisons of how sleep behavior varies across different demographic categories.

# Region is interesting for trend analysis, as it might reveal if sleep patterns differ by geography.

# Average Hours Sleep is the main metric being analyzed and will be compared across these categories to identify any insights.
