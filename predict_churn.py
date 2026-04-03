import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv('edtech_subscriptions.csv')

X = df[['Hours_Watched', 'Quizzes_Taken', 'Days_Since_Last_Login']]
y = df['Churned']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("--- Machine Learning Model Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))
importance = model.coef_[0]
for i,v in enumerate(['Hours', 'Quizzes', 'Recency']):
    print(f'Feature: {v}, Score: {importance[i]:.4f}')