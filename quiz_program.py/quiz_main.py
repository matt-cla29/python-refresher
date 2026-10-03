import quiz
import video_games
import movie
import books
 
 
while True:
 
    # Show the quiz choices
    quiz.show_quizes()
 
    # Ask which category they want
    choice = int(input("\nchoose your quiz type: "))
 
 
    # Select the questions and answers
    if choice == 1:
        print("you have chosen the movie category")
        chosen_quiz = movie.Mquiz_questions
        right_answer = movie.Mquiz_answers
 
    elif choice == 2:
        print("you have chosen the book category")
        chosen_quiz = books.Bquiz_questions
        right_answer = books.Bquiz_answers
 
    elif choice == 3:
        print("you have chosen the video game category")
        chosen_quiz = video_games.Vquiz_questions
        right_answer = video_games.Vquiz_answers
 
    else:
        print("Invalid choice")
        continue
 
 
    # Start the selected quiz
    print("\nstarting selected quiz")
 
    score = 0
 
 
    # Ask all 5 questions
    for i in range(len(chosen_quiz)):
 
        print(f"\nQuestion {i + 1}:")
        print(chosen_quiz[i])
 
        user_answer = input("Your answer: ")
 
        if user_answer.strip().lower() == right_answer[i].strip().lower():
            print("next question")
            score += 1
 
        else:
            print("next question")
 
 
    # ONLY runs after all 5 questions
    print("\n=== QUIZ FINISHED ===")
    print(f"Your score: {score}/{len(chosen_quiz)}")
 
 
    # Ask whether they want another quiz
    end_quiz = input(
        "\nType yes for another quiz or no to finish: "
    ).strip().lower()
 
 
    if end_quiz == "no":
        print("Thanks for quizzing!")
        break
 
    elif end_quiz == "yes":
        print("\nTaking you back to quiz category choices.\n")
        continue
 
    else:
        print("\nInvalid answer. Ending quiz.")
        break

