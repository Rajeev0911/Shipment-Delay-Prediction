# Shipment Prediction API Documentation

## 1. Approach to Data Preparation and Model Selection

### Data Preparation

1. **Loading Data**: 
   The dataset is loaded from a CSV file named `data.csv`.

2. **Handling Missing Values**: 
   - The `Vehicle Type` column is filled with its most common value to handle missing data.

3. **Feature Engineering**: 
   - `Shipment Date` is converted to a datetime object, and new features such as `Month`, `Day`, and `Weekday` are extracted.
   
4. **Encoding Categorical Variables**: 
   - Categorical columns such as `Vehicle Type`, `Origin`, `Destination`, `Weather Conditions`, and `Traffic Conditions` are encoded using Label Encoding.

5. **Target Variable**: 
   - The target variable `Delayed` is converted into a binary numeric form: 'Yes' to 1 and 'No' to 0.

6. **Feature Selection**: 
   - Irrelevant columns such as `Shipment ID`, `Shipment Date`, `Planned Delivery Date`, and `Actual Delivery Date` are dropped.

### Model Selection

1. **Logistic Regression**: 
   - A Logistic Regression model is used as the base classifier to predict shipment delays.
   - Features are fed into the model, and predictions are generated.

2. **Random Forest**: 
   - A Random Forest classifier with 100 estimators is used to predict shipment delays.
   - The model is trained and evaluated using the training and testing data.

3. **Model Evaluation**: 
   - Both Logistic Regression and Random Forest models are evaluated using classification reports.

4. **Saving the Model**: 
   - The Random Forest model is saved using `joblib` for future use.

---

## 2. API Functionality and Usage Instructions

### API Overview

- **API Name**: Shipment Prediction API
- **Base URL**: `http://localhost:8000`

### Endpoints

#### 1. Home Endpoint

- **URL**: `/`
- **Method**: GET
- **Description**: 
  - Provides a welcome message.

  ```json
  {
    "message": "Welcome to Shipment Prediction API"
  }
