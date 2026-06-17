import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
dtypes = {
    'Hours_Watched': 'float32',
    'Quizzes_Taken': 'uint16',
    'Days_Since_Last_Login': 'uint16',
    'Churned': 'uint8'
}
df = pd.read_csv('edtech_subscriptions.csv', dtype=dtypes)

X = df[['Hours_Watched', 'Quizzes_Taken', 'Days_Since_Last_Login']]
y = df['Churned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(n_jobs=-1)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)

print("--- Machine Learning Model Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))
importance = model.coef_[0]
for i, v in enumerate(['Hours', 'Quizzes', 'Recency']):
    print(f'Feature: {v}, Score: {importance[i]:.4f}')
