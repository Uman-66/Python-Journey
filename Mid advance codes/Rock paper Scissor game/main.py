from draw import *
game= [rock,paper,scissor]
def main():
    choice=int(input("Welcome to the rock paper and scissor game, write 0 for the rock,1 for the paper,2 for the scissor"))
    if choice<0 or choice>2:
        print("invalid number")
    else:
        print(game[choice])
        import random
        computer=random.randint(0,2)
        print(game[computer])
        if choice ==0 and computer==2 or choice ==1 and computer==0 or choice ==2 and computer==1:
            print("You win")
        elif choice==computer:
            print("its a draw")
        else:
            print("You lose")


while True:
    main()