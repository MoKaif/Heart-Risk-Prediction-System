# Heart Risk Prediction with Machine Learning


This project aims to develop an end-to-end machine learning model for heart risk prediction using Flask. By leveraging a dataset of patient information and applying machine learning techniques, this model can predict the risk of heart-related issues.

## Features

- **Data preprocessing:** The dataset is processed to handle missing values, perform feature scaling, and handle categorical variables using appropriate techniques.
- **Machine learning algorithms:** Various machine learning algorithms, such as logistic regression, decision trees, and random forests, are implemented to train and evaluate the heart risk prediction model.
- **Model evaluation:** The model is evaluated using performance metrics like accuracy, precision, recall, and F1-score to assess its effectiveness.
- **Web application:** A web application is built using Flask to provide an intuitive user interface for interacting with the trained model.

## Dataset

The dataset used in this project contains various attributes related to patients' medical information, including age, gender, blood pressure, cholesterol levels, and more. The dataset is preprocessed to ensure data quality and integrity.

Data contains;
- Age - age in years
- Sex - (1 = male; 0 = female)
- ChestPainType - chest pain type
- RestingBP - resting blood pressure (in mm Hg on admission to the hospital)
- Cholesterol - serum cholestoral in mg/dl
- FastingBS - (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- RestingECG - resting electrocardiographic results
- MaxHR - maximum heart rate achieved
- ExerciseAngina - exercise induced angina (1 = yes; 0 = no)
- oldpeak - ST depression induced by exercise relative to rest
- ST_Slope - the slope of the peak exercise ST segment
- HeartDisease - have disease or not (1=yes, 0=no)
