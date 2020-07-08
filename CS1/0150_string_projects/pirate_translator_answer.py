print("Welcome to the pirate translator. Say something and I will")
text = input("translate it into piratese.")
text = text.replace("ar", "Arrgh!")
text = text.replace("er", "Arrgh!")
text = text.replace("you", "ye")
text = text.replace("friend", "scurvy dog")
text = text+", ye scurvy dog!"
print(text)