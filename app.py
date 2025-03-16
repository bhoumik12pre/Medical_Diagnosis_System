# app.py (Main Flask Application)
from flask import Flask, render_template, request
from knowledge_base import MedicalDiagnosis
from experta import Fact

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        symptoms = request.form.get('symptoms').strip().lower().split(',')
        engine = MedicalDiagnosis()
        engine.reset()

        for symptom in symptoms:
            engine.declare(Fact(symptom=symptom.strip()))

        engine.run()

        # Correctly extract diagnosis and treatment
        diagnosis = next((fact['diagnosis'] for fact in engine.facts.values() if 'diagnosis' in fact), "No diagnosis available.")
        treatment = next((fact['treatment'] for fact in engine.facts.values() if 'treatment' in fact), "Consult a healthcare provider.")

        return render_template('result.html', diagnosis=diagnosis, treatment=treatment)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
