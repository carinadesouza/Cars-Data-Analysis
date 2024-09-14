import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
sns.set(color_codes=True)
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

## load the csv file 
df = pd.read_csv("Cars_data.csv")

## print the head of the dataframe
print(df.head())

# Get the datatypes of each columns number of records in each column.
print(df.info())

# List of columns to drop
cols_to_drop = ["Engine Fuel Type", "Market Category", "Vehicle Style", "Popularity", "Number of Doors", "Vehicle Size"]

# Dropping the specified columns
df = df.drop(columns=cols_to_drop)

# Displaying the updated dataframe
print(df.head())

# Dictionary containing old column names as keys and new column names as values
rename_dict = {
    "Make": "Brand",
    "Model": "Car_Model",
    "Year": "Manufacture_Year",
    "Engine HP": "Horsepower",
    "Engine Cylinders": "Cylinders",
    "highway MPG": "Highway_MPG",
    "city mpg": "City_MPG",
    "MSRP": "Price"
}

# Renaming the columns using the rename function
df = df.rename(columns=rename_dict)

# Displaying the updated dataframe
print(df.head())

# Counting the number of rows before removing duplicates
initial_row_count = df.shape[0]

# Removing duplicate rows
df = df.drop_duplicates()

# Convert 'Transmission Type' column to lowercase
df['Transmission Type'] = df['Transmission Type'].str.lower()
# Counting the number of rows after removing duplicates
final_row_count = df.shape[0]

# Displaying the counts
print(f"Number of rows before removing duplicates: {initial_row_count}")
print(f"Number of rows after removing duplicates: {final_row_count}")
print(f"Number of duplicate rows removed: {initial_row_count - final_row_count}")

# Checking for missing values in the dataframe
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Dropping rows where 'Horsepower' and 'Cylinders' have NaN values
df = df.dropna(subset=["Horsepower", "Cylinders"])

# Verifying if the missing values were dropped
missing_values_after_drop = df.isnull().sum()
print("\nMissing values after dropping rows:\n", missing_values_after_drop)



# Select only numeric columns from the DataFrame
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate Q1 (25th percentile) and Q3 (75th percentile) for numeric columns only
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1


# Create a boxplot for each numerical feature to visualize outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()
# Create a boolean DataFrame indicating outliers
is_outlier = (numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))

# Remove rows where any column has outliers
df_no_outliers = df[~is_outlier.any(axis=1)]

print(f"Shape of the dataframe before removing outliers: {df.shape}")
print(f"Shape of the dataframe after removing outliers: {df_no_outliers.shape}")

plt.figure(figsize=(10, 6))
sns.histplot(df['Horsepower'], kde=True, bins=30)  # kde=True adds the density plot
plt.title('Histogram and Density Plot of HP')
plt.xlabel('Horsepower')
plt.ylabel('Frequency')
plt.show()



# Assuming 'df' is your DataFrame and it contains the 'Make' column
# Count the number of cars for each make
make_counts = df['Brand'].value_counts()

# Optional: Get the top 'n' makes if you want to limit the number of bars
top_makes = make_counts.nlargest(10)  # Adjust the number as needed

# Plot the histogram
plt.figure(figsize=(12, 8))
top_makes.plot(kind='bar', color='skyblue')  # Bar plot with color
plt.title('Number of Cars by Brand')
plt.xlabel('Brand')
plt.ylabel('Number of Cars')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()
print(df.head(10))

# Create a subplot with 2 columns
plt.subplot(1, 2, 1)  # (rows, cols, panel number)

sns.countplot(data=df, x='Transmission Type', palette='viridis')  # Count plot for Transmission
plt.title('Count Plot of Transmission')
plt.xlabel('Transmission')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability


plt.subplot(1, 2, 2)  # (rows, cols, panel number)
sns.countplot(data=df, x='Driven_Wheels', palette='viridis')  # Count plot for Drive Mode
plt.title('Count Plot of Drive Mode')
plt.xlabel('Drive Mode')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plots
plt.tight_layout()
plt.show()



# Assuming 'df' is your DataFrame and it contains 'HP' and 'Price' columns

# Create a scatter plot to visualize the relationship between 'HP' and 'Price'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Horsepower', y='Price', alpha=0.7, color='blue')  # Adjust alpha and color as needed
plt.title('Scatter Plot of HP vs Price')
plt.xlabel('Horsepower)')
plt.ylabel('Price')
plt.grid(True)
plt.show()



# Bar plot showing the mean Price across different Cylinders
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Cylinders', y='Price', estimator='mean', ci=None, palette='viridis')  # Palette is optional
plt.title('Mean Price across Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Mean Price')
plt.grid(True)
plt.show()


# Bar plot showing the median Price across different Cylinders
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Cylinders', y='Price', estimator=np.median, ci=None, palette='coolwarm')
plt.title('Median Price across Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Median Price')
plt.grid(True)
plt.show()

# Count plot showing the number of cars in each Cylinder category
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Cylinders', palette='pastel')
plt.title('Number of Cars by Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Count')
plt.grid(True)
plt.show()


# Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show() 

df.to_excel('Cars_data_Final_Dataset.xlsx', index=False)