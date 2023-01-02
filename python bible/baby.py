from random import choice

questions = ["Why is the sky blue?: ",
             "What is your favorite color?: ",
             "What happened to the dinosaurs?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh... Okay")
