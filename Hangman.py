import random
words = ["gucci", "prada", "marni", "louboutin", "chanel", "fendi"]
def choose_random_word(words): #define a function
    word = random.choice(words) #created a variable for computer to chose a random word
    while "_" in word or " " in word:
        word = random.choice(words) #created loop to ask computer to iterate until all the _ has been filled
    return word.upper()

print("Welcome to Hangman!")
word = choose_random_word(words)
dashes = list(word) # convert an iterable string into a list.
display_list = []

for each in dashes:
    display_list.append("_")

count = len(word)
guesses = 0
user_letter = 0
used_list = []

while count != 0 and user_letter != "exit":
    print(" ".join(display_list))
    user_letter = input("Guess your letter: ")

    if user_letter.upper() in used_list:
        print("Oops! Already guessed that letter.")
    else:
        for each_letter in range(0,len(word)):
            if user_letter.upper() == word[each_letter]:
                display_list[each_letter] = user_letter.upper()
                count -= 1
        guesses += 1
    used_list.append(user_letter.upper())

if user_letter == "exit":
    print("Thanks!")
else:
    print(" ".join(display_list))
    print("Good job! You figured that the word is "+word+" after guessing %s letters!" % guesses)