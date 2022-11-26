word="secret"
allowed_errors=7
guesses=[]
done=False
while not done:
    for i in  (word):
        if i.lower() in guesses:
            print(i,end=" ")
        else :
            print("_", end="")
    print(" ")
    guess=input("try to guess: ")
    guesses.append(guess.lower())
    if guess not in word:
        allowed_errors-=1
        if allowed_errors==0:
            break
    done=True
    for letter in word:
        if letter not in guesses:
            done=False
if done:
    print(f"you have found a word {word}")
else:
    print(f"game over! the word was {word }  ")



