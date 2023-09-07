def Teacher_Question(teacher1, teacher2):
    
    teacher1 = input("please enter your favorite teacher: ")
    teacher2 = input("please enter your next favorite teacher: ")

    if teacher1 == "Sekol" and teacher2 != "Wright":
        print(f"That is right. the best theacher is {teacher1}")
    elif teacher1 == "Wright" or teacher2 == "Wright":
        print("Wrong. -500000 points for you")
    elif teacher1 != "Sekol" or teacher2 != "Sekol":
        print(f"I suppose {teacher1}, and {teacher2} are acceptable")
    elif teacher1 == "none" or teacher2 == "none":
        print("pick something please")
    else:
        print("I'm not sure what you answered but the correct answer is always 42")