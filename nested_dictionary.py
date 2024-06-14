student = {
    "name": "John",
    "score": {
        "chemistry": 98,
        "physics": 85,
        "math": 97,
    },
}
print(student["score"]["physics"])
print(student.keys())  # returns dict_keys
print(student.values())  # returns dict_values
print(student.items())  # returns dict_items (key,value) pairs as tuples
print(student.get("score"))  # returns the key according to the value
new_student = {"name": "Sara", "score2": 85}
student.update(new_student)
print(student)
print(student.get("score2"))  # returns with no error
# print(student("score2")) --> error message
# print(student.update(new_student)) # instead of student, we can use new_student
