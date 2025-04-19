questions = {
  "What is the capital of France?":"b",
  "Which language is used to write python?":"a",
  "What does CPU stand for?":"c"
 }

options = [
    ["a) Berlin", "b) Paris", "c) Madrid"],
    ["a) Python", "b) HTML", "c) CSS"],
    ["a) Central Programming Unit", "b) Control Panel Unit",
      "c) Central Processing Unit"]
]

score = 0
for i, question in enumerate(questions):
    print(f"\n{question}")
    for option in options[i]:
        print(option)
    answer = input("Enter your answer (a/b/c): ").lower()
    if answer == questions[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\n Your final score is: {score}\{len(questions)}")
