#must only stop for guesses
#"Please enter your next guess: "
import random
import time

# Open up and read the txt file
wordlist = open("word_list.txt", "r")

# Grab the words and make a list
gamewords = wordlist.read().splitlines()

# Grab random word
word = (random.choice(gamewords)).lower()
words_guessed = [] # to tell player what they've used so far
tries = 7 # lives
secretword = "*" * len(word) #display the correct number of stars
print(secretword) #print the word.. but hidden



while (tries == 7) and secretword != word: # do this loop while you still have enough lives and teh word hasnt been guessed. only for first question
    
    newsecretword = "" # for us to update the word and replace with correct letters
    guess = input("Please enter your guess: ")
    
    #stop useing same letter 
    if guess in words_guessed:
        print("you have already used this letter")
        


    #if the letter is in the word 
    elif guess in word:

        print (f"{guess} is in the word!")
        words_guessed.append(guess)
        
        # enumerate teh word and insert letter at correct index
        for i, ch in enumerate(word):
            if ch == guess:
                newsecretword += ch
            else:
                newsecretword += secretword[i]
        secretword = newsecretword
 
    # deduct a life for a wrong guess
    else: 
        print(f"{guess} is not in the word!")
        tries -= 1
        words_guessed.append(guess)

    print(f"Words guessed so far: {words_guessed}")
    print(f"Tries remaining: {tries} ")

    print(secretword + "\n \n \n")

# same as above but for the rest of the guesses
while (tries > 0) and secretword != word:
    
    newsecretword = ""
    guess = input("Please enter your next guess: ")
    
    
    if guess in words_guessed:
        print("you have already used this letter")
        


    
    elif guess in word:

        print (f"{guess} is in the word!")
        words_guessed.append(guess)
        
        for i, ch in enumerate(word):
            if ch == guess:
                newsecretword += ch
            else:
                newsecretword += secretword[i]
        secretword = newsecretword
 

    else: 
        print(f"{guess} is not in the word!")
        tries -= 1
        words_guessed.append(guess)

    print(f"Words guessed so: {words_guessed}")
    print(f"Tries remaining: {tries} ")

    print(secretword + "\n \n \n")

# if you have lost all your lives
if tries == 0:
	print(f"\n  You lose. The word was '{word}'" )
	time.sleep(5)

# if you guess the word
if secretword == word:
	print(f"\n  Congradulations you win")
	time.sleep(5)




            


        













