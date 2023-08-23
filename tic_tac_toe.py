import random
board={"tl":"","t":"","tr":"",
           "ml":"","m":"","mr":"",
           "ll":"","l":"","lr":""} 
    
def TheBoard(board):
    print(board["tl"]+" | "+board["t"]+" | "+board["tr"])
    print("- + - + -")
    print(board["ml"]+" | "+board["m"]+" | "+board["mr"])
    print("- + - + -")
    print(board["ll"]+" | "+board["l"]+" | "+board["lr"])
choice=True
TheBoard(board)
while choice:
    choice=input("Enter whether you want X or O ")
    if choice == "X" or choice=="x":
        choice="X"
        break
    elif choice == "O" or choice=="o" :
        choice="O"
        break
    else:
        print("choose again,Invalid choice")
    

comp_entry=random.randint(0,9)
def input_user():
    Entry=input("Enter the area you want to place it in")
    if Entry=="1 " or Entry=="tl":
        board["tl"]=choice
    elif Entry=="2" or Entry=="t":
        board["t"]=choice
    elif Entry=="3" or Entry=="tr":
        board["tr"]=choice
    elif Entry=="4" or Entry=="ml":
        board["ml"]=choice
    elif Entry=="5" or Entry== "m":
        board["m"]=choice 
    elif Entry=="6" or Entry=="mr":
        board["mr"]=choice
    elif Entry=="7" or Entry== "ll":
        board["ll"]=choice
    elif Entry=="8" or Entry=="l":
        board["l"]=choice
    elif Entry=="9" or Entry=="lr":
        board["lr"]=choice
    else:
        pass

def setup():
    for i in range(0,11):
        input_user()
        TheBoard(board)

setup()