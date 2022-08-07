print("Welcome to the Love Calculator!")

print("..... (¯`v´¯)♥")
print(".......•.¸.•´")
print("....¸.•´")
print("... (")
print(" ☻/")
print("/▌♥♥")
print("/ \ ♥♥")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_name = (lower_name1 + lower_name2)
digit1 = lower_name.count("t")
digit2 = lower_name.count("r")
digit3 = lower_name.count("u")
digit4 = lower_name.count("e")
digits_first = (digit1 + digit2 + digit3 + digit4)

digit5 = lower_name.count("l")
digit6 = lower_name.count("o")
digit7 = lower_name.count("v")
digit8 = lower_name.count("e")
digits_second = (digit5 + digit6 + digit7 + digit8)

score = int(str(digits_first) + str(digits_second))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
