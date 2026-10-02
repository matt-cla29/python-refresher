# ==== code ====

Mquizes_score = 0

Mquiz_questions = ["what creature can you not feed after midnight?: ",
"how many harry potter movies are there?: ",
"what famous christmas movie feature a boy being left at home by himself?: ",
"how many live action supermen are there?: ",
 "what horror character comes for you in your nightmares?: "]

Mquiz_answers = ["gremlin", "8", "home alone", "12", "freddy kreuger"]

for question, correct_answer in zip(Mquiz_questions,Mquiz_answers):
    user_reply = input(f"{question} ").lower().strip()
    
    if user_reply == correct_answer:
        print("next question")
        good_answer = Mquizes_score + 1
    else:
        print("next question")

print(good_answer)

 