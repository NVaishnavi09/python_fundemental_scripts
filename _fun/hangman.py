import random
list_word=['hibiscus','jasmine','lilly','sunflower','weather','eucaliptous','marigold']
word_choosen=random.choice(list_word)
word_length=len(word_choosen)
#print(word_choosen,word_length)
guesses=""
turns=10
#guess=input("enter the letter: ")
while turns>0:
    failed=0
    for char in word_choosen:
      if char in guesses:
        print("right")
      else:
        print("_")
        failed=failed+1

    if failed==0:
        print("You WIN")
        print(f"The word is {word_choosen}")
        break
    print()
    guess=input("guess a character: ")
    guesses+=guess

    if guess not in word_choosen:
        turns-=1
        print("wrong")
        print(f"You have {turns} left")

    if turns==0:
        print("You loose")
        print(f'{word_choosen} is the answer ')
        print( " END ")
        

        