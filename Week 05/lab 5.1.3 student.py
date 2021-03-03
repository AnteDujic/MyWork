# Program that stores a student name and list of courses and grades in a dict
    # It then prints the data
# Author: Ante Dujic



student = {
"name":"Mary",
"modules": [
{
"courseName":"Programming",
"grade": 45
},
{
"courseName":"History",
"grade":99
}
]
}

print ("Student: {}" .format(student["name"]))

for module in student["modules"]:
    print ("\t {} \t: {}" .format(module["courseName"], module["grade"]))