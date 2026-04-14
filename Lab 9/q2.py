from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define structure
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

# Prior probabilities
cpd_I = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_S = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.6], [0.4]]
)

cpd_D = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4], [0.6]]
)

cpd_G = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.7,0.5,0.4,0.3,0.4,0.2,0.2,0.1],  # A
        [0.2,0.3,0.4,0.4,0.4,0.5,0.3,0.2],  # B
        [0.1,0.2,0.2,0.3,0.2,0.3,0.5,0.7]   # C
    ],
    evidence=['Intelligence','StudyHours','Difficulty'],
    evidence_card=[2,2,2]
)

cpd_P = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.95,0.80,0.50],  
        [0.05,0.20,0.50]   
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)

print("Model Valid:", model.check_model())

infer = VariableElimination(model)


q1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours':0, 'Difficulty':0}
)

print("\nProbability of Pass given StudyHours=Sufficient and Difficulty=Hard:")
print(q1)


q2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass':0}
)

print("\nProbability of High Intelligence given Pass=Yes:")
print(q2)