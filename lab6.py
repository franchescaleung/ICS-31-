#Franchesca Leung 78831208 and Emily Chan 70161430. ICS 31 Lab sec 3. Lab Assignment 6.

#part c
print("---Part C---")
#c1
print()
print("c1")
print()
def contains(a:str, b:str) -> bool:
    '''returns true if b is in a, else false'''
    if b in a:
        return True
    else:
        return False

print(contains('bird', 'ird'))
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
assert contains('apple', 'app')
assert not contains('tree', 'tea')

#c2
print()
print("c2")
print()
def sentence_stats(a: str):
    '''takes string and prints stats'''
    space = 0
    characters = 0
    words = 0
    average = 0
    table = str.maketrans(".,?!@#$%^&*():", "              ")
    a = a.translate(table)
    l = a.split()
    total = 0 
    for word in l:
        total += len(word)
    words = len(l)
    for i in a:
        if i == " ":
            space +=1
    characters = len(a)
    average = total/words
    print("Characters: " + str(characters) + "\n" + "Words: " + str(words) + "\n" + "Average word length: " + str(average))

sentence_stats('I love UCI')
#c3
print()
print("c3")
print()
def initials(s:str) -> str:
    '''takes an input of a string representing a whole name and returns its initial in capital letters'''
    l = s.split()
    initials = ""
    for word in l:
        initials += word[0].upper()
    return initials

assert initials('Guido van Rossum') == 'GVR'
assert initials('Bill Cody') == 'BC'
assert initials('alan turing') == 'AT'

#part d
print("---Part D---")
#d1
print()
print("d1")
print()
from random import randrange
for i in range(50):
    print (randrange(11))
print()
for i in range(50):
    print(randrange(1, 7))

#d2
print()
print("d2")
print()
def roll2dice() -> int:
    '''returns a number of two random dice roll'''
    x = (randrange(1, 7)) + (randrange(1, 7))
    return x
for i in range(50):
    print (roll2dice())

#d3
print()
print("d3")
def distribution_of_rolls(n: int):
    '''shows chances of rolls'''
    rolls = []
    for i in range(n):
        x = roll2dice()
        rolls.append(x)
    for i in range(2, 13):
        x = rolls.count(i)
        percent = (x/n) *100
        stars = "*" * x
        print('{:2}:{:6}({:4.1f}%)  {}'.format(i,x,percent,stars))
    print("-----------------------------" + "\n" + str(n) + " rolls")
    
distribution_of_rolls(200)

#part e
print()
print("---Part E---")
print()
#e1
print("e1")
a = "abcdefghijklmnopqrstuvwxyz"
def rotate(key: int):
    '''return new alphabet'''
    rotate  = ""
    for letter in a:
        if letter in a:
            rotate += a[(a.index(letter) + key) % len(a)]
    return rotate
def shift_encrypt(message: str, key: int):
    '''return the ciphertext'''
    t = str.maketrans(a, rotate(key))
    return message.translate(t)
        
print(shift_encrypt("abc", 3))
def shift_decrypt(message: str, key: int):
    '''turns code into normal text'''
    #never tried
    key = 26 - key
    return shift_encrypt(message, key)
    

print(shift_decrypt("def", 3))

#e2
print()
print("e2")
print()
secretmessage= "ifmmp xpsme"
print(shift_decrypt(secretmessage, 1))
#hello world




#part f
a = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]
b = '''
"Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure." '''
print()
print("part f")
print()
#f1
print("f1")
def print_line_numbers(l: "list of strings"):
    '''takes a list of strings and prints string preceded by a line number'''
    i=1
    for item in l:
        print('{:2}:  {}'.format(i, item))
        i+=1

print_line_numbers(a)

#f2
print()
print("f2")
print()
def stats(l: "list of strings"):
    '''takes list of strings and prints stats'''
    emptylines = 0
    charperline = 0
    avgcharperline = 0
    lines = 0
    for i in l:
        if i == "\n":
            emptylines +=1
    for string in l:
        charperline += len(string)
        avgcharperline = charperline/len(l)
    for i in l:
        if i != "\n":
            lines +=1
            avgcharpernonemptyline = charperline/lines
    print('{:5}   {}'.format(lines, 'lines in the list'))
    print('{:5}   {}'.format(emptylines, 'empty lines'))
    print('{:7.1f} {}'.format(avgcharperline, 'average characters per line'))
    print('{:7.1f} {}'.format(avgcharpernonemptyline, 'average characters per non-empty line'))

stats(a)

#f3
print()
print("f3")


def list_of_words(s: str) -> "list of individual words":
    '''takes list of strings and returns a list of individual words'''
    table1 = str.maketrans("/.,\!@#?$\"%^&*()-", "                 ")
    l = s.translate(table1)
    words = l.split()   
    new = []
    for item in words:
        item = item.strip()      
        new.append(item)
    return new

assert(list_of_words("hello world.")) == ["hello", "world"]       
print(list_of_words(b))
    


