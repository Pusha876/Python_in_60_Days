import json

with open("question.json", 'r', encoding='utf-8') as file:
    content = file.read()
data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "wrong answer"
    message = (f"{result} {index + 1} - Your answer: {question['user_choice']}"
               f"Correct answer: {question['correct_answer']}")
    print(message)

print(score, "/", len(data))
