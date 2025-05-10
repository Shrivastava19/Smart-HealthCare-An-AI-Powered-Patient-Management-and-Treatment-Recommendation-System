# Smart-HealthCare-An-AI-Powered-Patient-Management-and-Treatment-Recommendation-System

This is a Flask-based web application designed for disease prediction and patient data management using machine learning. Users can register, log in, input symptoms, and receive predictions for possible diseases. The app also includes a basic AI chatbot and treatment recommendation section.

Features
User authentication (register & login)

Patient data entry and listing

Disease prediction using a trained machine learning model

Symptom-based analysis form

AI Chatbot interface

Treatment recommendation (placeholder)

Clean, responsive HTML UI

Technologies Used
Backend: Python, Flask

Frontend: HTML, CSS (inline)

ML Model: Scikit-learn (serialized as disease_model.pkl)

File Structure
bash
Copy
Edit
├── app.py                 # Main Flask application
├── train_model.py         # Script to train and export the disease prediction model
├── disease_model.pkl      # Trained machine learning model
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── patient_data.html
│   ├── disease_analysis.html
│   ├── chatbot.html
├── tempCodeRunnerFile.py  # Temporary script file (optional)
Getting Started
Prerequisites
Python 3.x

pip

Installation
Clone the repository or download the source code.

Install dependencies:

bash
Copy
Edit
pip install flask scikit-learn
Run the application:

bash
Copy
Edit
python app.py
Access it in your browser at http://127.0.0.1:5000

Train Your Own Model (Optional)
bash
Copy
Edit
python train_model.py
This script will generate a new disease_model.pkl.

Screenshots
Login/Register

Home Dashboard

Patient Data Entry

Disease Prediction Result

Chatbot Page

License
This project is for educational purposes.
