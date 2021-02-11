# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1.lower()
name2.lower()

name1_count = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")

name2_count = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

total_score_str = str(name1_count) + str(name2_count)
total_score = int(total_score_str)


if total_score < 10 or total_score > 90:
  print (f"You're score is {total_score}, you go together like coke and mentos.")
elif total_score < 50 and total_score > 40:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}")
