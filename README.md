# Medical Insurance Cost Prediction

## 📌 Project Overview

Medical insurance costs can vary based on several personal and lifestyle-related factors. This project focuses on analyzing medical insurance data and predicting insurance charges based on age.

The project includes exploratory data analysis, data visualization, correlation analysis, and an interactive Streamlit application.

## 🎯 Objectives

* Analyze the medical insurance dataset.
* Understand patterns and relationships within the data.
* Perform exploratory data analysis.
* Analyze correlations between different variables.
* Build a prediction system for estimating medical insurance charges.
* Develop an interactive Streamlit web application.

## 📊 Dataset

The dataset contains information about individuals and their medical insurance charges.

### Main Attributes

* **Age** – Age of the individual.
* **Sex** – Gender of the individual.
* **BMI** – Body Mass Index.
* **Children** – Number of dependent children.
* **Smoker** – Smoking status.
* **Region** – Residential region.
* **Charges** – Medical insurance charges.

## 🔍 Exploratory Data Analysis

The project performs exploratory analysis to understand the dataset and identify important patterns.

The analysis includes:

* Dataset structure and information
* Missing value analysis
* Statistical summary
* Age distribution
* Insurance charge distribution
* Age versus insurance charges
* BMI versus insurance charges
* Insurance charges based on smoking status
* Correlation analysis

## 📈 Data Visualization

The project uses visualizations to understand relationships and distributions within the dataset.

Visualizations include:

* Histograms
* Scatter plots
* Box plots
* Correlation heatmap



## 🤖 Machine Learning Models

The project implements and compares multiple machine learning models for predicting medical insurance charges:

### 1. Linear Regression

Used to establish a basic relationship between the input features and medical insurance charges. It provides a simple and interpretable prediction approach.

### 2. Ridge Regression

A regularized regression technique that helps reduce the effect of multicollinearity and improves model stability.

### 3. Lasso Regression

A regularized regression technique that can reduce the influence of less important features and perform feature selection.

### 4. Decision Tree Regression

A tree-based regression method that captures non-linear relationships between the input variables and insurance charges.

### 5. Random Forest Regression

An ensemble learning technique that combines multiple decision trees to produce more robust predictions and handle complex relationships in the data.

### Model Evaluation

The models are evaluated and compared using regression performance metrics such as:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**

The model with the best overall performance is selected for the prediction application.


### Output

**Predicted Medical Insurance Charges**

The model learns the relationship between age and insurance charges from the available dataset and provides an estimated charge for a given age.

## 🌐 Streamlit Application

An interactive Streamlit application is developed for the prediction system.

The user can:

1. Enter an age.
2. Click the **Predict** button.
3. View the estimated medical insurance charges.

The application provides a simple and user-friendly interface for interacting with the prediction system.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

## 📁 Project Structure

```text
-MedicalInsurance/
│
├── app.py
├── insurance.csv
├── requirements.txt
└── README.md
```

## ⭐ Key Features

* Medical insurance dataset analysis
* Exploratory data analysis
* Correlation analysis
* Data visualization
* Insurance charge prediction
* Interactive Streamlit interface
* Simple and easy-to-use application
