'''
ICS 31 Winter 2018 Lecture 2
Hardware- laptop, phone, disc, monitor
software
programs recipies for the computer
code is the text
syntax is the grammer rules
semantics: meaning of what's going on


'''
'''
name = input("What's your name, user? ")
print("Your name is", name)
print(name, "What's your age")
age = int(input())
print("Your age is", age, name)
student_age = 17
print(name, "you are older than me by", age - student_age, "years")

'''
'''
variable types

nouns - objects
verbs are actions
operator- +, -, *
function

'''
'''

print("ICS31 is " + "fun")
print("Ho"*3) #This is what Santa says

'''

print ("how big is the damage? ") # use space to avoid awkward spacing when printing answer
cost = int(input())
tip_percent = 20
tip = cost * tip_percent/100
total = cost + tip
print("Total cost $", total)
