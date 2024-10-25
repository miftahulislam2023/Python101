""" marks = {"Math": 78, "English":89, "Bangla":56}
print(marks["Bangla"])
print(marks["Math"])
 """

students = [
    {"name": "Miftah", "Math": 89, "English":89, "Bangla":67},
    {"name": "Zahid", "Math": 95, "English":92, "Bangla":78},
    {"name": "Shishir", "Math": 69, "English":56, "Bangla":88}
    ]

for x in range(0, 3):
    sum = students[x]["Math"] + students[x]["English"] + students[x]["Bangla"]
    print(students[x]["name"], sum)