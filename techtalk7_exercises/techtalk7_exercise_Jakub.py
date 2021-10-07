student_list = ['pam','rob','joe','greg','bob','amy','matt']

print(student_list[2:5])
print(student_list[:-5])
print(student_list[5:])
print(student_list[0:6])
if any('rob' in s for s in student_list):
    print(student_list[1])