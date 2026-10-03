# ===== code ======

quiz_choices = ["movie", "books", "video games"]

def show_quizes():
    print("\nwhat quiz do you want?: ")

    for number in range(len(quiz_choices)):
        print(number + 1, "-", quiz_choices[number])



