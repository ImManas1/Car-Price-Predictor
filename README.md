# Car Price Predictor

This project is a machine learning based web application that predicts the selling price of a used car using features such as company, kilometers driven, fuel type, transmission type, owner type, and seller type.

The project covers the complete pipeline including data cleaning, feature engineering, model training, evaluation, and deployment using Flask.

## Project Overview

- Predicts the selling price of used cars
- Implements a complete machine learning pipeline
- Uses a trained regression model with preprocessing
- Provides a web interface using Flask
- Model and preprocessing steps are saved using pickle

## Machine Learning Approach

### Models Evaluated

- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- K-Nearest Neighbors Regressor  
- Decision Tree Regressor  
- Random Forest Regressor  

### Final Model

- Scikit-learn Pipeline
- ColumnTransformer with OneHotEncoder
- Lasso Regression

## Model Performance

- R² Score: approximately 0.51  
- RMSE: approximately 277,000  
- MAE: approximately 167,000  
