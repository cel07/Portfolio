# Concrete Compressive Strength Prediction
## Project Overview
This project aims to predict the compressive strength of concrete based on various components such as cement, water, superplasticizer, and the age of the concrete. The objective is to use machine learning models to find the best predictor for compressive strength, helping to optimize concrete mixture compositions.

Concrete compressive strength is a key factor in construction and infrastructure projects. The ability to accurately predict this strength helps in improving the efficiency of material usage and ensuring safety standards are met.

## Motivation
Predicting concrete compressive strength is important in the construction industry to ensure quality and durability. Accurately predicting how strong a concrete mix will be can help optimize resources, reduce costs, and improve safety. This project explores various machine learning techniques to achieve this goal.

## Dataset
The dataset used for this project includes multiple samples of concrete mixtures with the following features:

 - Cement (kg in a m^3 mixture)
 - Blast Furnace Slag (kg in a m^3 mixture)
 - Fly Ash (kg in a m^3 mixture)
 - Water (kg in a m^3 mixture)
 - Superplasticizer (kg in a m^3 mixture)
 - Coarse Aggregate (kg in a m^3 mixture)
 - Fine Aggregate (kg in a m^3 mixture)
 - Age (days)
 - Compressive Strength (MPa, megapascals) - This is the target variable we are predicting.
The dataset is stored in the data/ directory.

## Project Workflow
1. Data Preprocessing:
 - Load and clean the dataset.
 - Handle missing values and outliers.
 - Perform feature scaling (if needed) and log transformations for skewed data.
2. Exploratory Data Analysis (EDA):
 - Analyze the distribution of each feature.
 - Visualize the relationships between the features and the target variable.
 - Identify the most important features for predicting compressive strength.
3. Modeling:
 - Experiment with different models including:
 - Linear Regression
 - Polynomial Regression (degree 2, 3, 4, and 5)
 - Perform cross-validation and hyperparameter tuning to find the best model.
4. Model Evaluation:
 - Evaluate model performance using metrics such as:
   - R² Score: Indicates how well the model captures the variability in compressive strength.
   - Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values.
 - Generate learning curves to understand how the model behaves with different amounts of training data.
5. Results:
 - The Polynomial Regression (degree 4) model performed the best, achieving an R² score of 0.80 on the validation set. This means the model can explain 80% of the variance in compressive strength based on the provided features.
 - Visualizations such as the scatter plot of actual vs. predicted values and learning curves are included in the reports/figures folder.


## Key Results
 - Best Model: The Polynomial Regression (degree 4) model gave the highest prediction accuracy with an R² score of 0.80.
 - Insights: The model successfully captured non-linear relationships between the features and compressive strength. Cement and superplasticizer were found to be highly correlated with strength, while water content had a negative impact on strength.
 - Outliers: The model struggled with predicting compressive strength for some high-strength concrete samples, indicating potential areas for improvement.
