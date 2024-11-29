# 29. Simple Quiz

ques = [
    "How many days are in a year?: ",
    "When WW2 started? (year): ",
    "What is the main color of Japan flag: ",
]

ans = ["365", "1939", "white"]
score = 0
for i in range(len(ques)):
    if input(ques[i]) == ans[i]:
        score += 1
print(score)
