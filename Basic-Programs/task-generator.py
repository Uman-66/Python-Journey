loop_on = True
reallist = []
while loop_on:
    do = input("If you want to add a task press a, if wanna see your todo list press e, if you did something and wanna delete from todo list press d, and if want to exit press x")

    if do == "a":
        task = input("What do you want to add?")
        list.append(task)

    elif do == "e":
        for i in range(len(list)):
            print(list[i])

    elif do == "x":
        print("Goodbye")
        loop_on = False

    elif do == "d":
        for i in range(len(list)):
            print(f"{i+1}: {list[i]}")

        done = int(input("Which task do you want to delete?, mention its number"))-1

        if done >= 0 and done < len(list):
            removed = list.pop(done)
            print(f"{removed} was removed")

