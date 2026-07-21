from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.3], [0.7]]
)

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.9, 0.5],  
        [0.1, 0.5]    
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,
    values=[
        [0.8, 0.6],   
        [0.2, 0.4]   
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_fatigue = TabularCPD(
    variable='Fatigue',
    variable_card=2,
    values=[
        [0.7, 0.3],  
        [0.3, 0.7]    
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_chills = TabularCPD(
    variable='Chills',
    variable_card=2,
    values=[
        [0.6, 0.4],   
        [0.4, 0.6]    
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

# Add all CPTs
model.add_cpds(
    cpd_disease,
    cpd_fever,
    cpd_cough,
    cpd_fatigue,
    cpd_chills
)

print("Model Valid:", model.check_model())

infer = VariableElimination(model)

q1 = infer.query(
    variables=['Disease'],
    evidence={
        'Fever': 0,
        'Cough': 0
    }
)

print("\nTask 1: P(Disease | Fever=Yes, Cough=Yes)")
print(q1)

q2 = infer.query(
    variables=['Disease'],
    evidence={
        'Fever': 0,
        'Cough': 0,
        'Chills': 0
    }
)

print("\nTask 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
print(q2)

q3 = infer.query(
    variables=['Fatigue'],
    evidence={
        'Disease': 0
    }
)

print("\nTask 3: P(Fatigue=Yes | Disease=Flu)")
print(q3)