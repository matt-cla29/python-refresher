import movie
import quiz
import video_games
import books

quiz.show_quizes()

choice = int(input("\nchoose your quiz type: "))

index = choice - 1

quiz = quiz.names[index]