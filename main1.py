student_data = {
"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1
"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}
a = []
b = {}
for i,j in student_data.items():
    unique = (j["name"],j["class"],j["subject_integration"])
    if unique not in a: 
        a.append(unique)
        b[i]=j
print(a)
print(b)