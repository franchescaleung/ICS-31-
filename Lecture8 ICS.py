## Lecture 8 ICS 31 Winter 2018
## Next time - in class exercise

names = ["Donald", "Mother", "Mickey"]
for name in names: #for each loop
    print ("Dear", name, end= "***")

surnames = ["Duck", "Goose", "Mouse"]

for i in range (min(len(names), len(surnames))):
    print (names[i], surnames[i])

for i in range (7):
    print(i)

for i in range (1980, 2018):
    print (i)

for i in range (1880, 1920, 4):
    print("year", i)

for i in range (1880, 1920, 4):
    if (i % 100 != 0):
        print("leap year", i)

for i in range (10, 0, -1):
    print(i)
print("Blast off")


def square(num_list: "list of numbers") -> "list _of_numbers":
    "create a list of squares"
    result = [ ]
##   num_list[0] = int(input("give me a number"))
    for i in num_list:
        result.append(i*i)
    return result
assert square ([ ]) == [ ]
assert square ([4]) == [16]
assert square ([5, -1]) == [25, 1]

print (square([7, 11, 25, 32]))

word = input("Give me a word ")
long_word = "catalog"
if word in long_word:
    print(word, "is in", long_word)
else:
    print(word, "isn't in", long_word)

'''if year > 0 and year < 2200:
    is_leap_year'''
print(not True)
print(not False)


