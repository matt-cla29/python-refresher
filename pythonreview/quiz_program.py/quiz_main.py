#========== code ===========

import video_games
import quiz
import movie
import books

quiz.show_quizes()

chosen_quiz = None

choice = int(input("\nchoose your quiz type: "))

index = choice - 1

quiz = books.Bquiz_questions[index]
quiz = movie.Mquiz_questions[index]
quiz = video_games.Vquiz_questions[index]


if choice == 1:
    print("you have chosen the book category")
    chosen_quiz = books.Bquiz_questions


elif choice == 2:
    print("you have chosen the movie category")
    chosen_quiz = movie.Mquiz_questions

elif choice == 3:
    print("you have chosen the video game category")
    chosen_quiz = video_games.Vquiz_questions

print("\nstarting selected quiz")

