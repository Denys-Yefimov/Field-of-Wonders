import random
attempts = int(input("Enter the number of attempts\n"))
word = ["apple", "banana", "orange", "blueberry"]
random_word = random.choice(word)
guessed_word = "*" * len(random_word)
print(guessed_word)

answer_right_word = ["Bingo!", "You're right!", "You guessed it!", "That's correct!"]
rn_answer_right_word = random.choice(answer_right_word)


print(f"start, the word consists of {len(random_word)} letters")

whole_word = ""
while attempts > 0:
    letter = input("Enter either a single letter ir a whole word\n").lower()

    if letter == random_word:
        print(rn_answer_right_word)
        print("You win")
        break

    elif letter in random_word:
        print(rn_answer_right_word)
        new_guessed_word = ""
        for i in range(len(random_word)):
            if random_word[i] == letter:
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[i]
        guessed_word = new_guessed_word
        print(new_guessed_word)
        if new_guessed_word == random_word:
            print("win")
            break
    else:
        print("This is not true word")
        attempts -= 1
        print(f"You've got {attempts} attempt left")



    # if letter not in random_word:
    #     print("There is not letter")
    #     attempts -= 1
    #     print(f"You've got {attempts} attempt left")
    if attempts == 0:
        print("you lose")
        break
