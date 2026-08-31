student_data = {
    "id1": {"name": "Alex", "class": "10A", "subject": "Math"},
    "id2": {"name": "Jordan", "class": "10B", "subject": "Science"},
    "id3": {"name": "Alex", "class": "10A", "subject": "Math"},
    "id4": {"name": "Taylor", "class": "10A", "subject": "History"},
}
print(student_data)
print("getting id1:", student_data.get("id1", "Not Found"))
print("getting id5 before adding:", student_data.get("id5", "Not Found"))
student_data["id5"] = {"name": "Morgan", "class": "10C", "subject": "Art"}
print("added id5:")
print(student_data)
student_data["id2"]["subject"] = "Physics"
print("updated id2 subject:", student_data["id2"])
cleaned_data = {}
seen_records = []
for student_id, details in student_data.items():
    record = (details["name"], details["class"], details["subject"])
    if record not in seen_records:
        seen_records.append(record)
        cleaned_data[student_id] = details
student_data = cleaned_data
print("cleaned data without duplicates:")
print(student_data)
student_data.pop("id4")
print("amount of records left:", len(student_data))
print("final list of students:")
for student_id, details in student_data.items():
    print(
        f"{student_id}: {details['name']} - {details['class']} - {details['subject']}"
    )