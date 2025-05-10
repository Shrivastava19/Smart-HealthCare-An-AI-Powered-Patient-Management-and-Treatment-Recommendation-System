# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Example dataset
data = {
    'symptoms': [
        'fever cough sore throat',
        'headache nausea light sensitivity',
        'body pain infection',
        'fever loss of taste',
        'stomach ache and diarrhea'
    ],
    'disease': ['Flu', 'Migraine', 'Infection', 'COVID-19', 'Infection']
}
df = pd.DataFrame(data)

# Vectorization and model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['symptoms'])
y = df['disease']

model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
with open('disease_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)
