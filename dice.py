from random import randint
print('''
 ____  _            ____  _                 _       _             
|  _ \(_) ___ ___  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
| | | | |/ __/ _ \ \___ \| | '__ ` __ \| | | | |/ _` | __/ _ \| '__|
| |_| | | (_|  __/  ___) | | |  |  | | | |_| | | (_| | || (_) | |   
|____/|_|\___\___| |____/|_|_|  |__| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                
''')
choice = ' '
while True:
    choice = input("Do you wish to roll the die[Y/N]").upper()
    if choice == "N":
        print("Exiting the program")
        break
    elif choice == "Y":
        print("Rolling the die")
        choice_disp = randint(1, 6)
        if choice_disp == 1:
            print('''
             _____
            /__   |
               |  |
               |  |   
               |  |  
               |  |        
            ___|  |___  
           |__________|
            ''')
        elif choice_disp == 2:
            print('''
             ________
            /______  \ 
                   |  |
                  /  /
                 /  /  
                /  /        
            ___/  /___  
           |__________|
            ''')
        elif choice_disp == 3:
            print('''
            _________
           |_______  |
                   | |
            _______| |
           |_______  |
                   | |   
            _______| |
           |_________|
            ''')
        elif choice_disp == 4:
            print('''
           __     __
          |  |   |  | 
          |  |   |  |
          |  |___|  |
          |______|  |
                 |  | 
                 |  |
                 |__|
            ''')
        elif choice_disp == 5:
            print('''
            _________
           |  _______|
           |  |
           |  |______
           |_______  |
                   | |
            _______| |       
           |_________|
            ''')
        else:
            print('''
            _________
           |  _______|
           |  |
           |  |______
           |         |
           |         |
           |_________|
            ''')
    else:
        print("only accepts Y or N as an input")
