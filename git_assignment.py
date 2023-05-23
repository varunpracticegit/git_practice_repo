students = ['Varun', 'Abhishek', 'Manjeet']
files = ['projectmi_main', 'project_util', 'project_data']

if len(students) != len(files):
    print("Error: Number of students and files doesn't match")
else:
    for i in range(len(students)):
        student = students[i]
        file = files[i]
        print(f"{student} will create {file}.py")