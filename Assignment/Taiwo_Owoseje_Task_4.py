# Task 1: Your Favourite Life Quote
quote = input("What is your favourite quote: ")
print(f"\"{quote.title()}\"")

# Task 2: Shopping List Manager
foodlist = []
foodlist1 = input("Please enter your first item: ")
foodlist2 = input("Please enter your second item: ")
foodlist3 = input("Please enter your third item: ")
foodlist.append(foodlist1)
foodlist.append(foodlist2)
foodlist.append(foodlist3)
print(f"Your items: {foodlist} are now added to cart. ")

# Task 3: Word Counter
speech = input("What have you eaten today: ")
switch = speech.split()
wcount = len(switch)
print(wcount)

# Task 4: Name Organizer
name = input("Enter 5 names, separated by spaces: ")
name_sp = name.lower().split(" ")
name_sp.sort()
print(name_sp)
[print(f"{name}") for name in name_sp]

# Task 5: Student score Tracker
stnames = []
stscores = []
student = input("Write 3 student names:")
score = input("Write the scores of the students:")
stnames.append(student)
stscores.append(score)
print(f"{stnames}\t\n{stscores}\t\n")

# Task 6: Word Analyser
analyse = input("Enter a word: ") 
upperc = analyse.isupper()
print(f"the word is in upper case: {upperc}")
lowerc = analyse.islower() 
print(f"the word is in lower case: {lowerc}") 
titlec = analyse.istitle()
print(f"the word is in lower case: {titlec}")
print(analyse[::-1])


# Task 7: List Maniputalation
cityname = ["Jalingo", "Ibadan", "Abeokuta", "Ikeja", "Bobape"]
print(f"{cityname} are the cities on the itinerary, change Abeokuta to any other city of your choice" )
cityname_request = str(input("Enter a city of your choice: "))
cityname.remove("Abeokuta")
cityname.insert(2, cityname_request)
cityname.remove("Bobape")
cityname.insert(0, "Abuja")
print(cityname)