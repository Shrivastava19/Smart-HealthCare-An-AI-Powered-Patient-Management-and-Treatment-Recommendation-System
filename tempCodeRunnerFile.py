from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import random
import pickle
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy users
users = {'admin@example.com': {'password': 'admin123'}}

# Dummy patient data
patients = []

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Load ML model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), 'disease_model.pkl')
with open(model_path, 'rb') as f:
    vectorizer, ml_model = pickle.load(f)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            login_user(User(email))
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in users:
            users[email] = {'password': password}
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/patient_data', methods=['GET', 'POST'])
@login_required
def patient_data():
    if request.method == 'POST':
        patient = {
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'symptoms': request.form['symptoms']
        }
        patients.append(patient)
    return render_template('patient_data.html', patients=patients)

@app.route('/disease_analysis', methods=['GET', 'POST'])
@login_required
def disease_analysis():
    disease = None
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        disease = predict_disease(symptoms)
    return render_template('disease_analysis.html', disease=disease)

def predict_disease(symptoms):
    X_input = vectorizer.transform([symptoms])
    prediction = ml_model.predict(X_input)
    return prediction[0]

@app.route('/treatment_recommendation', methods=['GET', 'POST'])
@login_required
def treatment_recommendation():
    treatment = None
    if request.method == 'POST':
        disease = request.form['disease']
        treatment = recommend_treatment(disease)
    return render_template('treatment_recommendation.html', treatment=treatment)

def recommend_treatment(disease):
    treatment_plans = {
        'COVID-19': 'Rest, isolation, antiviral medications',
        'Flu': 'Rest, hydration, over-the-counter meds',
        'Migraine': 'Pain relievers, dark room rest',
        'Infection': 'Antibiotics, doctor consultation'
    }
    return treatment_plans.get(disease, 'General Check-up Recommended')

@app.route('/chatbot', methods=['GET', 'POST'])
@login_required
def chatbot():
    response = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot_response(user_input)
    return render_template('chatbot.html', response=response)

def chatbot_response(user_input):
    default_responses = [
        "I'm not a doctor, but you should get some rest.",
        "Consider visiting a healthcare professional.",
        "Stay hydrated and monitor your symptoms.",
        "Health is wealth. Take care!"
    ]
    return random.choice(default_responses)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
