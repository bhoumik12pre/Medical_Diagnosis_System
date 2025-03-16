from experta import *

class MedicalDiagnosis(KnowledgeEngine):

    @Rule(AND(Fact(symptom='fever'), Fact(symptom='cough'), Fact(symptom='fatigue')))
    def flu(self):
        self.declare(Fact(diagnosis="Flu"))
        self.declare(Fact(treatment="Rest, hydration, and fever-reducing medications."))

    @Rule(AND(Fact(symptom='sore throat'), Fact(symptom='runny nose')))
    def cold(self):
        self.declare(Fact(diagnosis="Common Cold"))
        self.declare(Fact(treatment="Drink warm fluids and take rest."))

    @Rule(AND(Fact(symptom='headache'), Fact(symptom='nausea'), Fact(symptom='blurred vision')))
    def migraine(self):
        self.declare(Fact(diagnosis="Migraine"))
        self.declare(Fact(treatment="Avoid bright lights and take prescribed medications."))
