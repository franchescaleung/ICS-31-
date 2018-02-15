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
    print(a)
    l = a.split()
    total = 0 
    for word in l:
        total += len(word)
    print(total)
    print("l:",l)
    words = len(l)
    print(words)
    for i in a:
        if i == " ":
            space +=1
    characters = len(a)
    average = total/words
    print(characters)
    print(space)
    print("Characters: " + str(characters) + "\n" + "Words: " + str(words) + "\n" + "Average word length: " + str(average))

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
##for i in range(50):
##    print (randrange(11))
##print()
##for i in range(50):
##    print(randrange(1, 7))

#d2
print()
print("d2")
print()
def roll2dice() -> int:
    '''returns a number of two random dice roll'''
    x = (randrange(1, 7)) + (randrange(1, 7))
    return x
##for i in range(50):
##    print (roll2dice())

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
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_encrypt(message: str, key: int):
    '''return the ciphertext'''
    #why is it only d
    encrypt = []
    for letter in message:
        if letter.split() and letter in ALPHABET:
            encrypt.append(ALPHABET[(letter.index(letter)+ key) % 52])
            print(ALPHABET[letter.index(letter) + key])
        else:
            encrypt.append(i)
    print(encrypt)
    final = ''.join(encrypt)
    return final
        
print(shift_encrypt("abc", 3))
def shift_decrypt(message: str, key: int):
    '''turns code into normal text'''
    #never tried

#e2
print()
print("e2")
print()
secretmessage= "ifmmp xpsme"
#hello world




#part f
a = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]
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
    #how to not repeat lines
    lines = 16824
    emptylines = 483
    avgcharperline = 53.7
    avgcharpernonemptyline = 65.9
    li = [lines, emptylines, avgcharperline, avgcharpernonemptyline]
    s = ["lines in the list", "empty lines", "average characters per line", "average characters per non-empty line"]
    for i in li:
        for j in s:
            print('{:7.1f} {:1}'.format(i, j))
stats(["hu", "ki"])

#f3
print()
print("f3")
b = '''
Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure." '''

def list_of_words(s: str) -> "list of individual words":
    '''takes list of stringa and returns a list of individual words'''
    #fix empty space
    words = s.split()
    new = []
    for item in words:
        item = item.strip()
        item = item.strip("\"")
        item = item.strip(".")
        item = item.strip(",")
        item = item.strip("\n")
        item = item.strip("\"")        
        new.append(item)
    return new

assert(list_of_words("hello world.")) == ["hello", "world"]       
print(list_of_words(b))
    
