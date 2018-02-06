#Namedtuples
#step 1: set it up (say this once at the top of the program:
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
print (student_list)
print()
print(student_list[2])
print(student_list[-2])
my_favorite_student = student_list[0]
type(my_favorite_student)
print ("My favorite student is", my_favorite_student.name)

student_list.sort()
print()
print (student_list)


student_list = [student_2, student_1, student_3]
sorted_list = sorted(student_list)
print(student_list)
print()
print(sorted_list)

print()
any_string = 'abcdef'
any_string[2] = "x"

'''
MUTABLE list
IMMUTABLE strings
'''
