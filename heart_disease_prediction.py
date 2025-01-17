# -*- coding: utf-8 -*-
"""heart_disease_prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UdK1YowQEyFBxj-1K-3j-Qq0x2jXCNp-
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
heart_data = pd.read_csv('/content/Heart_Disease_Prediction.csv')

# Preprocessing
# Encoding categorical variables (e.g., Sex, Chest pain type, Thallium, and Heart Disease)
label_encoder = LabelEncoder()
heart_data['Sex'] = label_encoder.fit_transform(heart_data['Sex'])
heart_data['Chest pain type'] = label_encoder.fit_transform(heart_data['Chest pain type'])
heart_data['Thallium'] = label_encoder.fit_transform(heart_data['Thallium'])
heart_data['Heart Disease'] = label_encoder.fit_transform(heart_data['Heart Disease'])

# Splitting the data into features (X) and target (y)
X = heart_data.drop(columns='Heart Disease')
y = heart_data['Heart Disease']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Model prediction
y_pred = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')
print('Classification Report:')
print(report)
print('Confusion Matrix:')
print(conf_matrix)



















