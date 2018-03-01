# Franchesca Leung 78831208 and Yujie Wang 33065328. ICS 31 Lab sec 3. Lab asst 8.

#part c
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
#c.1
print("c1")
def read_menu_with_count(f: "filename") -> "list of dishes":
    '''takes file, reads file, returns a list of Dish structures created from the data'''
    infile = open(f, "r")
    dishes = []
    count = 0
    for i in infile:
        if count>=1:
            a = i.split("\t")
            dish = Dish(a[0], str(a[1]), str(a[2].strip()))
            dishes.append(dish)
        count+=1
    infile.close()
    return dishes


##print(read_menu_with_count("menu2.txt"))

#c.2
print()
print("c2")

def read_menu(f: "filename") -> "list of dishes":
    '''takes file, reads file, returns a list of Dish structures created from the data'''
    infile = open(f, "r")
    dishes = []
    count = 0
    for i in infile:
        a = i.split("\t")
        dish = Dish(a[0], str(a[1]), str(a[2].strip()))
        dishes.append(dish)
        count +=1
    infile.close()
    return dishes
##print(read_menu("menu3.txt"))

#c.3
print()
print("c3")
def write_menu(l: "list of dishes", f: "filename") -> None:
    '''write the dish data to the named file'''
    outfile = open(f, "w")
    outfile.write(str(len(l)))
    outfile.write("\n")
    for dish in l:
        for att in dish:
            outfile.write(str(att) + "\t")
        outfile.write("\n")
    outfile.close()
    return

dish1 = Dish("Chicken", "$14.99", "450")
dish2 = Dish("Samosa", "$12.00", "300")
a = [dish1, dish2]
write_menu(a, "b.txt")


#Part D
print()
print("---Part D---")
print()
Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
studentBody = [sW, sX, sY, sZ]
#d.1
print("d1")
def students_at_level(l: "list of students", level: str) -> "list of students":
    '''takes list of students and returns students with matching class level'''
    matched = []
    for student in l:
        if student.level == level:
            matched.append(student) #all attributes
    return matched
print(students_at_level(studentBody, "FR"))

#d.2
print()
print("d2")
def students_in_majors(l: "list of students", s: "list of strings") -> "list of students":
    '''takes lists of students and returns students who have a major listed in s'''
    matched = []
    for student in l:
        if student.major in s:
            matched.append(student) #all attributes
    return matched
print(students_in_majors(studentBody, ["PSB", "CS"]))

#d.3
print()
print("d3")
print()


def course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return c1.dept == c2.dept and c1.num == c2.num
def course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    for course in SL:
        if course_equals(course, c):
            return True
    return False
    
def student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    cour = Course(department, coursenum, "", "", 0)
    return course_on_studylist(cour, S.studylist)
    

    
def students_in_class(l: "list of students", dept: str, cour: int) -> "list of students":
    '''returns a list of students who are enrolled in specific dept and course'''
    enrolled = []
    for student in l:
        if student_is_enrolled(student, dept, cour):
            enrolled.append(student) #all attributes
    return enrolled
    
print(students_in_class(studentBody, "Writing", "39A"))

#d.4
print()
print("d4")
print()
def student_names(l: "list of Students") -> "list of names":
    '''takes a list of students and returns a list of just the names of those students'''
    names = []
    for student in l:
        names.append(student.name)
    return names
print(student_names(studentBody))

#d.5
print()
print("d5")
print()
print("1")
print(students_in_majors(studentBody, ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']))
print("2")
print(student_names(students_in_majors(studentBody, ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])))
print("3")
print((str(len(students_in_majors(studentBody, ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])))) + " student(s) in this major")
print("4")
##fix
print(student_names(students_in_majors(students_at_level(studentBody, "SR"), ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])))
print("5")
print(len(students_in_majors(students_at_level(studentBody, "SR"), ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])))
print("6")
print((str(len(students_in_majors(students_at_level(studentBody, "SR"), ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']))/len(students_in_majors(studentBody, ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])))) + " %")
print("7")
#number of freshman in ics major

a = students_in_majors(students_at_level(studentBody, "FR"), ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])
enroll = 0
for student in a:
    if student_is_enrolled(student, "ICS", "31"):
        enroll +=1
print(enroll)
print("8")
b = students_at_level(studentBody, "FR")
s = 0
g=0
for student in b:
    if student_is_enrolled(student, "ICS", "31"):
        g +=1
        for c in student.studylist:
            s += c.units
            
print(s/g)
    
            
    
    
