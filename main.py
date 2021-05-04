 
import random
end_of_game = False
lives = 6 
from hangman_words import word_list
chosen_world = random.choice(word_list)
from hangman_art import logo
print(logo)
chosen_list= list(str(chosen_world))
empty_list = []
new_list =[]
length_chosen = len(chosen_world)
for i in range(length_chosen) :
  empty_list.append("_")
while end_of_game==False :
  guess = input("Guess a letter: ").lower()
  if guess in new_list :
    print("You guess this word before. Please write a different guess")
  else:
    for n in range(length_chosen) :
      letter = chosen_list[n]
      if letter == guess :
       empty_list[n] = guess
    print(f"{' '.join(empty_list)}")
    if guess not in chosen_list :
        print(f"{guess} is not in the word")
        from hangman_art import stages
        print(stages[lives])
        if lives == 0:
          print("You lose")
          print(chosen_world)
          break
        lives -= 1   
  new_list.append(guess)    
  if "_" not in empty_list:
      end_of_game = True
      print("You win.")


