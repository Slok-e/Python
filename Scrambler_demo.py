#The Magic Name Creator
import random
#Introduction
game = True
while game:
    
    def intro():
        print(' \n                    Welcome to the Magic Name \n                        Speak your name! \n                    to learn your Magic Name! \n', )
        n = 60
        print(str('_')* n)
        First_name = input('\n                Please Enter your First Name!\n ')
        Last_name = input('\n                Please Enter your Last Name!\n ')
        Name = First_name + Last_name
#Mixing names together and shuffling to produce random name
        Name_list = list(Name)
        random.shuffle(Name_list)
        aftermath = ''.join(Name_list)
#For Dramatic flair
        print(' \nBehold! \n \n' + First_name)
        print(Last_name)
        print(' \n Your magic name is...\n')
        print(' !!', aftermath.capitalize(),'!! \n')
#Code for continuation
    intro()

    game_on = input('\n Would you like to try again? Y/N \n')
    if game_on == ['Y','y','Yes','yes']:
        continue;
    else:
        
        print('Thanks for trying my Magic Name Game')
        break




        
      

