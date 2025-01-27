#ask user to input name
username = input("what is your name: ").title()
username = username.strip() #removing white spaces at the beginning or end of the username (accidental or not)
display = len(username)
display2 = len(username.split())
first_word = username.split()[0]
last_word = username.split()[-1]
first_three = username[:3]
last_three = username[-3:]
display_reverse = username[::-1]
display_reverse = "".join(reversed(username))
replace = username.replace(" ", "-")

print(username)
print(display)
print(display2)
print(first_word)
print(last_word)
print(first_three)
print(last_three)
print(display_reverse)
print(username.upper())
print(username.lower())
print(replace)
