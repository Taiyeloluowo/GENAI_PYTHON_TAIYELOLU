# single quotes
name = 'Ada'
print(name)

# double quotes
greeting = "Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssw0rd123"
print(password)

word = "Python"
print(word[2])   #p
print(word[-3])  #n

word = "Python"
print(word[0:4])  # Pyth
print(word[2:])   # thon
print(word[:3])   # Pyt
print(word[::2])  # Pto
print(word[::-1]) # nohtyP

a = "Hello"
b = "World"
print(a + " " + b)   # Hello World

word = "Hi! "
print(word * 3)      # Hi! Hi! Hi!

text = "Python programming"
print("Python" in text)     # True
print("Java" not in text)   # True

text = "Hello World"
print(text.find("o"))        # 4
print(text.rfind("o"))       # 7

text = "Hello World"
print(text.index("World"))   # 6

filename = "data.csv"
print(filename.startswith("data"))   # True
print(filename.endswith('.csv'))     # True

name = "Ada Balogun"
print(name.upper())

sentence = "PYTHON IS AMAZING"
print(sentence.lower())

text = "    Abuja    "
print(text.strip())

message = "I love Java"
print(message.replace("Java", "Python"))

text = "Hello ABEOKUTA"
print(text.swapcase())

test = "    Nigeria"
print(test.lstrip())

text = "Nigeria    "
print(text.rstrip())

fruits = "mango orange banana"
print(fruits.split())

text = "one,two,three,four"
print(text.rsplit(",", 2))

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

words = ["I", "love", "Python"]
print(" ".join(words))

text = "Python"
print(text.center(20, "-"))

text = "Python"
print(text.rjust(10, "*"))

num = "42"
print(num.zfill(9))

print("Lagos".isalpha())      #True
print("Lagos123".isalpha())   #False

print("12345".isdigit())
print("123a".isdigit())

print("Python3".isalnum())  # True
print("Python 3".isalnum())

original_string = "hello"
reversed_string = original_string[::-1]
print(reversed_string)

orig = "generative"
reve = orig[::-1]
print(reve)

original_string = "world"
reversed_string = "".join(reversed(original_string))
print(reversed_string)

orig = "generative"
reve = "".join(reversed(orig))
print(reve)
