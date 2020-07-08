import random

#http://www.pythonforbeginners.com/code-snippets-source-code/magic-8-ball-written-in-python/

options = ["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]

question = True
while question:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    answers = random.randint(0,7)
    print(options[answers])
