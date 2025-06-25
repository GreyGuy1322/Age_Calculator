age = int(input("Enter your AGE:\n"))  # Taking age

present_year = int(input("Enter the Present Year:\n"))  # Taking current year

# Age in desired year
newage = int(input("To know your age in desired YEAR, type the Year\nवांछित वर्ष में अपनी आयु जानने के लिए वह वर्ष टाइप करें:\n"))
print("Your age in desired year will be:")
print((newage - present_year) + age)

# Year when user will be of a desired age
c = int(input("To know the year in which you will be of that age 🤔\n(Type The Desired Age to get the year)\nउस वर्ष को जानने के लिए जिसमें आप उस उम्र के होंगे\n"))
print("You Entered Age:", c)
print("In", c - age + present_year, "You Will Be Of that Age")

# 100-year-old calculator
hund = int(input("Press 1 to know when you'll be 100\n"))
if hund == 1:
    print("In", present_year - age + 100, "You Will Be Of 100 😂\nQuite Old🧐...RIGHT")
else:
    print("YOU ENTERED WRONG NUMBER :(\nRestart The Program")

# Nice ending
print("Thank You For Trying Our Program\nHave A Good Day\n:)\nRegards DEV😊")
