from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Load dataset from a CSV file
data = pd.read_csv("data/stress_anxiety_depression_large_dataset.csv")

# Map column names to relatable questions
questions = {
    "interest": "How often have you felt a lack of interest in your daily activities?",
    "depressed": "How frequently do you feel down, depressed, or hopeless?",
    "sleep": "Do you often face trouble falling or staying asleep, or do you sleep too much?",
    "fatigue": "Do you feel tired or have little energy often?",
    "appetite": "How often do you experience poor appetite or overeating?",
    "worthlessness": "How often do you feel worthless or that you've let yourself or others down?",
    "concentration": "Do you often find it difficult to concentrate on tasks, like reading or watching TV?",
    "restlessness": "Have you noticed being unusually fidgety or restless recently?",
    "suicidal": "Do you have thoughts that you might be better off dead or have thoughts of self-harm?",
    "stress_level": "Do you frequently have panick attacks?",
    "anxiety_level": "Do you frequently feel nervous, restless, tense, or irritable?",
    "depression_level": "Do you frequently think about past events, or replaying mistakes in your mind?"
}

# Prepare the data
X = data.drop(columns=["mental_state"])
y = data["mental_state"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("form.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    # Get form data
    form_data = request.form
    input_data = [int(form_data[key]) for key in questions.keys()]

    # Predict mental state
    prediction = model.predict([input_data])[0]

    # Render the result page
    return render_template("result.html", mental_state=prediction)

if __name__ == "__main__":
    app.run(debug=True)
