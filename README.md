
# Exploratory Data Analysis on Cars Dataset

## Project Overview
This project focuses on conducting **Exploratory Data Analysis (EDA)** on a Cars dataset from Kaggle. The dataset contains various features such as make, model, year, engine, and more, which are used to predict car prices. The analysis identifies trends, removes outliers, and prepares the data for model building by handling missing values and cleaning irrelevant features.

## Dataset
The dataset includes the following key features:
- `Make`: Car manufacturer
- `Model`: Car model
- `Year`: Launch year
- `Engine Fuel Type`: Type of fuel used by the engine
- `Engine HP`: Horsepower of the engine
- `Transmission Type`: Manual or Automatic transmission
- `Driven_Wheels`: Type of wheel drive (e.g., All-Wheel Drive, Front-Wheel Drive)
- `MSRP`: Manufacturer's suggested retail price (Target variable)

## Key Steps

### 1. Data Cleaning
- Dropped irrelevant columns (`cols_to_drop`) that do not contribute to predicting car prices.
- Handled missing and duplicate values for better data consistency.
- Renamed columns for better clarity and understanding.

### 2. Outlier Detection
- Used the **Interquartile Range (IQR)** method to detect and remove outliers.

### 3. Visualization
- Visualized data through **box plots**, **histograms**, and **scatter plots** to understand the distribution of numerical variables.
- Created **bar plots** and **count plots** to observe the relationships between categorical and numerical variables.

### 4. Correlation Analysis
- Generated a **correlation heatmap** to identify strong and weak relationships between the features.

## Dashboard Creation
A **dashboard** will be created using **Tabular**, which will provide interactive and dynamic views of the key insights and data visualizations from the analysis. The dashboard will allow users to explore the relationships between features and make informed predictions about car prices.

## Libraries Used
- `pandas`: Data manipulation and cleaning
- `numpy`: Numerical computations
- `seaborn` and `matplotlib`: Data visualization
- `scipy`: Statistical analysis
- `tabular`: Dashboard creation for interactive exploration

## Conclusion
The EDA process successfully cleaned the dataset, visualized relationships between features, and prepared the data for future machine learning models. Outliers and missing values were appropriately handled, ensuring that the dataset is ready for further analysis. The **Tabular** dashboard will offer users a comprehensive and interactive way to explore the data.

