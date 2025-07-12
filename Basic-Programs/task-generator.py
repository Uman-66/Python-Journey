loop_on = True
real= []
while loop_on:
    do = input("If you want to add a task press a, if wanna see your todo list press e, if you did something and wanna delete from todo list press d, and if want to exit press x")

    if do == "a":
        task = input("What do you want to add?")
        real.append(task)

    elif do == "e":
        for i in range(len(real)):
            print(real[i])

    elif do == "x":
        print("Goodbye")
        loop_on = False

    elif do == "d":
        for i in range(len(real)):
            print(f"{i+1}: {real[i]}")

        done = int(input("Which task do you want to delete?, mention its number"))-1

        if done >= 0 and done < len(real):
            removed = real.pop(done)
            print(f"{removed} was removed")

