# 27. Basic To-Do List

myToDo = []

opr = ""
while opr != "q":
    opr = input("Enter an operation (v-view, a-add, r-remove): ")
    if opr == "v":
        print("\n".join(myToDo))
    elif opr == "a":
        myToDo.append(input("Add a To Do: "))
    elif opr == "r":
        myToDo.pop(int(input("Which one? indexs (1 to n): ")) - 1)
        print("Deleted succesfully!")
    else:
        print("Operation was wrong!. Try again")
