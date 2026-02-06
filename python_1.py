name : str =  "Rafi Afsan"
age : int = 24
print(name)
print(age)
Employment_status : bool = True

title : str = "I am a python programmer, I love coding and I am passionate about learning new technolgies. I am always looking for new opportunities to grow."
print(f"My name is {name} and I am {age} years old. {title}. My employment status is {Employment_status}")

MAX_AGE : int = 100
print(F"The maximum age is {MAX_AGE}")

print(f"Upper case: {title.upper()}")
print(f"Capitalized: {title.capitalize()}")
print(f"Lower case: {title.lower()}")

Employment_status : bool = True

print(f"Replace the word python with java: {title.replace('python','java')}")
print(f"Find the index of the word programmer in title : {title.find('programmer')}")

print(f"Split the title into a list of words: {title.split()}")

print(f"print the first 10 characters of the title: {title[:10]}")
print(f"print the first 10 words of the title : {' '.join(title.split()[:10])}")

print(f"print the last 10 characters of the title: {title[-10:]}")
print(f"print the last 10 words of the title : {' '.join(title.split()[-10:])}")

print(f"print the middle 10 characters of the title: {title[50:60]}")
print(f"print the middle 10 words of the title : {' '.join(title.split()[10:16])}")


first = "Rafi"
last = "Afsan"
print(f'My name is {first} {last}')
print(first+" "+last)
print(first * 5)