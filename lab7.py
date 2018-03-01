# Nicole Q Thai 55729939 and Franchesca Leung 78831208. ICS 31 Lab sec 3. Lab assignment 7.


#Part C
print("---Part C---")
print()
#c1-c3
from random import randrange
print("c1 to c3")
def random(f: "file") -> list:
    '''random from file'''
    infile1 = open(f, "r")
    y = infile1.readlines()
    name = []
    for i in y:
        name.append(i.split()[0].capitalize())
    infile1.close()
    return name[randrange(0, len(name))]
                

def random_names(i: int) -> list:
    ''' returns return names'''
    name = []
    for fullname in range(i):
        a = []
        a.append(random("surnames.txt"))
        x = randrange(0,1)
        if x == 0:
            a.append(random("femalenames.txt"))
        if x == 1:
            a.append(random("malenames.txt"))
        b = ', '.join(a)
        name.append(b)
        
    return name
    
print(random_names(4))
    

#Part D
print()
print("---Part D---")
print()
#d1
print("d1")
print()
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
        
def shift_decrypt(message: str, key: int):
    '''turns code into normal text'''
    key = 26 - key
    return shift_encrypt(message, key)
def shift_break(c: str) -> str:
    '''takes ciphertext string and returns the plaintext for the string'''
    dictionary = open("wordlist.txt", "r")
    dic = dictionary.read()
    g = []
    n = len(c.split())
    for num in range(26):
        i = 0
        word = shift_decrypt(c, num).split()
        for b in word:
            check = b.strip("/.,\!@#?$\"%^&*()-")
            if check in dic:
                i += 1
        if i == n:
            break
    dictionary.close()
    return ' '.join(word)
assert shift_break("ifz zpv") == "hey you"
    
                    
#d2
print()
print("d2")

print (shift_break("ifz, ibwf b ojdf ebz"))

        
#Part E
print("---Part E---")
#e1
def copy_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()


#e2/3/4
print()
def copy_file(s: str):
    '''copies file'''
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    i = 1
    write = False
    emptylines = 0
    charperline = 0
    avgcharperline = 0
    li = 0
    avgcharpernonemptyline = 0
    y = infile.readlines()
    for line in y:
        if s == "Gutenberg trim":
            if "*** END" in line:
                break
            if write:
                outfile.write(line)
            if "*** START" in line:
                write = True
                
        elif s == "line numbers":
            outfile.write("{:>5}: ".format(str(i)))
            outfile.write(line)
            i +=1

        else:
            outfile.write(line)
    if s == "statistics":
        for line in y:
            outfile.write(line)
        for i in y:
            if i == "\n":
                emptylines +=1
        for string in y:
            charperline += len(string)
            avgcharperline = charperline/len(y)
        for i in y:
            if i != "\n":
                li +=1
                avgcharpernonemptyline = charperline/li
        lines = len(y)
        g= ('{:5}   {}'.format(lines, 'lines in the list \n'))
        l = ('{:5}   {}'.format(emptylines, 'empty lines \n'))
        n = ('{:7.1f} {}'.format(avgcharperline, 'average characters per line \n'))
        k = ('{:7.1f} {}'.format(avgcharpernonemptyline, 'average characters per non-empty line'))
        print(g)
        print(l)
        print(n)
        print(k)
        outfile.write(g)
        outfile.write(l)
        outfile.write(n)
        outfile.write(k)
    infile.close()
    outfile.close()

#e5
print("e5")

copy_file("Gutenberg trim")
#copy_file("line numbers")
copy_file("statistics")
copy_file("l")
