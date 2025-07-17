from draw import stages
import random
word_list = ["aardvark" ,"baboon","camel"]
lives=5
random_word=random.choice(word_list)


underscore=[]
for char in random_word:
    underscore.append("_")


end = False
print(underscore)

while end == False:
    user=input(f"Guess the word here, you have {lives} guesses left ").lower()

    if user in random_word:
        for i in range(len(random_word)):

            if random_word[i]==user:
                underscore[i]=user


    else:
        print(stages[lives])
        lives -= 1
    print(underscore)


    if lives == 0:
        print("you lose")
        end = True


    elif not "_" in underscore:
        end = True
        print("you win")