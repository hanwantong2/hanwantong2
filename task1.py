words = []
n = int(input("3"))

for i in range(n):
    word = input(" what ")
    words.append(word)

sentence = ' '.join(words)
print("what", sentence)

words = []

while True:
    word = input("stop ")
    if word.lower() == 'stop':
        break
    words.append(word)

sentence = ' '.join(words)
print("Wow! This is a rare word!", sentence)
word = input("wow")

if 'f' in word.lower():
    print("Wow! This is a rare word!")
else:
    print("Hmm, this is not a very rare word...")

import random


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    return expression


def evaluate_expression(expression):
    return eval(expression)


while True:
    expression = generate_expression()
    result = evaluate_expression(expression)

    user_answer = input(f"hanwantong ")
    if user_answer.isdigit() and int(user_answer) == result:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", result)
