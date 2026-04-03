import pandas as pd
import numpy as np

def generate_edtech_data(records=1000):
    np.random.seed(42)
    data = {
        'User_ID': range(1, records + 1),
        'Course_Category': np.random.choice(['Data Science', 'Web Dev', 'AI/ML', 'Marketing'], records),
        'Subscription_Type': np.random.choice(['Monthly', 'Yearly'], records, p=[0.7, 0.3]),
        'Subscription_Fee': np.random.randint(500, 5000, records),
        'Hours_Watched': np.random.randint(1, 100, records),
        'Quizzes_Taken': np.random.randint(0, 20, records),
        'Days_Since_Last_Login': np.random.randint(0, 60, records),
    }
    
    df = pd.DataFrame(data)
    df['Churned'] = ((df['Days_Since_Last_Login'] > 30) & (df['Hours_Watched'] < 10)).astype(int)
    
    df.to_csv('edtech_subscriptions.csv', index=False)
    print("Dataset 'edtech_subscriptions.csv' generated!")

generate_edtech_data()