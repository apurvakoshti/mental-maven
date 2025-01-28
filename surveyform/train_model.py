import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv('data/stress_anxiety_depression_large_dataset.csv')

# Preprocess the data
X = df.drop(['mental_state'], axis=1)  # Features
y = df['mental_state']  # Target

# Encode the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
import os
os.makedirs('model', exist_ok=True)

# Save the model and the label encoder
joblib.dump(model, 'model/mental_health_model.pkl')
joblib.dump(label_encoder, 'model/label_encoder.pkl')
