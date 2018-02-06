from collections import namedtuple
#Step 2: define what your object looks like
#a student has a name, ID, major, GPA
Student = namedtuple("Student", "name ID major GPA") #blueprint
#step 3: Create a couple of objects of this new type
student_1 = Student("Peter Anteater", "1111111", "ICS", 5.0)
#step 4: Refer to FIELDS as needed with dot notation:
#print("My GPA:", s1.GPA)
'''Why does Student start with an uppercase letter and s1 start with lowercase letter?'''
student_2 = Student ("Grace Hopper", "0000000", "CS", 5.1)
student_3 = Student("Bill Gates", "9999999", "HR", 3.0)
student_list = [student_2, student_1, student_3]
#print(student_list)
#print()
sorted_list_1 = sorted (student_list)
#print (sorted_list_1)
#print()
def student_id (apprentice):
    '''Return ID number of a student'''
    return apprentice.ID
assert student_id (student_2) == '0000000'
print(student_id(student_1))
