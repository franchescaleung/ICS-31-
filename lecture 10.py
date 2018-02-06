##Lecture 10 ICS 31 Winter 2018
## Strings
'''Text processing is way to make our input to look the way we want.

A string is made of zero or more characters
A character is any keystroke, including whitespace (space, tab, end-of-line)
'''
##Zero characters - empty string
"" '' '''''' """""" #all empty strings
print("the length is", len(""))
print("the length is", len(" "))
a = ""
b = "    "
print(a == b)

s = "      Donald Duck "
print("->" + s + "<-")
print(s)
print(" She said, 'It\'s dark'")
print("\\")
print("The length is", len("\\"))
#backslash is just one symbol(\)

s = "Mother Goose"
print(s, ".")
print(s + ".")
print(s, " the second", ".", sep = "")
print(s, "the second", ".", sep = "***")
print(s, "the second", ".", sep = "")
print(s, " the second", ".", sep = "\n")
#\n = new line

#String methods
print()
print("Does Go occur is Mother Goose?")
print("Go" in s)
print("go" in s)
print()
print("Where does Go occur in Mother Goose?")
print("Position number", s.find("Go"), "is the location")
print("Position number", s.find("go"), "is the location")
print()
print("Does s start with an m?")
print(s.startswith("mother"))
print()
print("Does s end with an e?")
print(s.endswith("e"))

m = "Mississippi"
print ("How many times does 's' occur in", m + "?")
print(m.count("s"))
print ("Change each s to OK")
print (m.replace ("s", "OK"))
print(m) #.replace creates new string


s = "FOURTH score and SeVen  (that's 87) Years AGO..."
print(s)
print(s.lower())
print(s.upper())
print(s.title())


text = ''' UCI is a wonderful place to be.
    I am so happy!
    to be  here! aaa'''

list_of_words = text.split()
print(list_of_words)


list_of_words = text.split("!")
print(list_of_words)
