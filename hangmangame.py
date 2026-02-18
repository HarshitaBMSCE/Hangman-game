import random

stages = ['''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___''',
    '''
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___''',
    '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
    _|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
    _|___''']

word_list = ["potato", "ironman", "annabelle", "shawn", "mathematics", "istanbul", "joker", "jigsaw", "natasha", "clint", "hulk", "loki"]
chosen_word = random.choice(word_list)

correct_letters = []
game_over = False
lives = len(stages) - 1

print(stages[0])  # Start with empty gallows

while not game_over:
    display = ""
    for i in chosen_word:
        if i in correct_letters:
            display += i
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
        break

    guessed = input("Enter a letter:\n").lower()

    if guessed in chosen_word:
        if guessed not in correct_letters:
            correct_letters.append(guessed)
    else:
        lives -= 1
        print("Wrong guess!")
        print(stages[len(stages) - lives - 1])

        if lives == 0:
            game_over = True
            print("You lose!")
            print("The word was:", chosen_word)
