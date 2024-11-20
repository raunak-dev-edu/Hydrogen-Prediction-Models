# Hydrogen Production Prediction Using Machine Learning

This project aims to predict hydrogen (H₂) production based on various input parameters such as temperature, pressure, biogas mass flow rate, and a combination of these features. The models were trained using Gradient Boosting Regressors (GBR) on datasets with different input parameters generated from sensitivity analyis on Aspen Plus, and the trained models are saved as pickle files for easy prediction.

## Project Overview

This project allows users to input values for specific parameters (temperature, pressure, biogas mass flow rate, or combinations of them), and the model will predict the corresponding hydrogen production. The user can choose the desired input parameter, and based on the selection, the model will predict the H₂ production.

## Features

- **Temperature-based prediction:** Model trained with temperature data to predict H₂ production.
- **Pressure-based prediction:** Model trained with pressure data to predict H₂ production.
- **Temperature and Pressure-based prediction:** Model trained with both temperature and pressure data to predict H₂ production.
- **Biogas mass flow-based prediction:** Model trained with biogas mass flow rate data to predict H₂ production.

## Model Training and Evaluation

The models are trained using Gradient Boosting Regressors (GBR) on different datasets. The evaluation process includes the following metrics:

- **Mean Squared Error (MSE):** Measures the average squared difference between predicted and actual values. A lower MSE indicates better model performance.
- **R² Score:** A statistical measure of how well the predictions match the actual data. An R² score closer to 1 indicates that the model explains most of the variance in the target variable.
- **Feature Importance:** The relative importance of each feature in predicting the target variable, as determined by the model.
- **Training vs Test Loss over Boosting Iterations:** The loss (Mean Squared Error) is computed at each boosting iteration, allowing us to track how the model's performance improves over time for both training and test sets.

The training results are saved as `.pkl` files, which can be used later for making predictions. These pickle files store the trained models, allowing you to load and use them without retraining.
