import re

string = "PythonExercisesPracticeSolution"
a = re.sub(r"(\w)([A-Z])", r"\1_\2", string).lower()

print(a if a else 'Not found')
