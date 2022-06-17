from question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Orange\n(c) Blue\n\n",
    "What color are bananas?\n(a) Purple\n(b) Yellow\n(c) Green\n\n",
    "What color are strawberries?\n(a) Red\n(b) Megenta\n(c) Black\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " right")

run_test(questions)