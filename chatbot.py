#Meet my Chatbot Friend Starter Code

#chatbot introduces themself
print("Hello! I'm Gabby the chatbot.")
name = input("What's your name? ")

print("Let's see if I can spell that:")

#Add Part 5 code here
name_list = list(name)
print(name_list)

for letter in name_list:
  print(letter)

print("Nice to meet you " + name)

#chatbot asks questions
print("Can you tell me about yourself?")

#add Part 2 Step 2 code in this section
print("Where are you from?")
place = input("You are from... ")
print("I'd love to visit " + place + " one day!")

print("What are you passionate about?")
passion = input("You are passionate about... ")
print("Whoa, that's amazing! " + passion + " is so cool! :o")

print("What is your personal goal?")
goal = input("You hope to... ")
print("I really admire your goal to " + goal + ". I know you can do it! :D")

#chatbot tells their story
#add Part 4 code here
while True:
  topic = input("What would you like to know about me? - home, passion, goal, or none? ")

  #add Part 3 code here
  if topic.lower() == "home":
    print("I come from a chilly planet far away! :D")

  elif topic.lower() == "passion":
    print("I LOVE learning all kinds of things! *_*")

  elif topic.lower() == "goal":
    print("I hope to help people through coding! :)")

  elif topic.lower() == "none":
    print("Oh, okay! ^_^ ")
    break;

  else:
    print("Sorry, I didn't catch that. ")

print("Thanks for chatting with me! See you soon!")
