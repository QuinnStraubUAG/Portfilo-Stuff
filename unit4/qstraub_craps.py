import random
def bets ():
    bets_v = input("Put in your bets: ")
    #This is return the bet
    return bets_v
  
  
def begining_bank():
    print("You have $100 so... Good luck")
    return 100
    
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    dice_sum = dice1 + dice2
    
    print("You rolled {} {} so you got {}".format(dice1,dice2,dice_sum))
    return dice_sum

def game_thing():
    roll = dice_roll()
    if (roll == 2 or roll == 3 or roll == 12):
        print("You lost")
        check = 0 #lose
    elif (roll == 7 or roll == 11):
        print("You Win")
        check = 1 #win
    else:
        check = 2 #point
    new_roll = 0
    point_roll = roll
    while (check == 2) and (point_roll != new_roll or new_roll != 7):
        new_roll = dice_roll()
        print ("Your roll was {} it rolled {} ".format(point_roll,new_roll))
        if point_roll == new_roll:
            print("You win your first and Second number matchs")
        elif new_roll == 7:
            print ("You lost you rolled 7")
        else:
            print("It's a draw let's keep going ontil you ether win or lose")
        
        
        #This doesn't work yet ... 
        
        
        
# def craps():
#     begining_bank()
#     bets ()
#     dice_roll()
#     game_thing_first(dice_roll)
#     game_thing_point(dice_roll, game_thing_first)

def craps():
    # b_bank = begining_bank()
    # print("You are going to strat with {} dollors".format(b_bank))
    # beats = bets()
    # print (beats)
   game = game_thing()
    
    
    
craps()
    
    
#work in progess
    
    
        
    
     
    
    
 # æææææææ ignorge 
  

  
#   If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends.
# If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends.
# If the player rolls any other number (a 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their “point number“
  
  
  
    
# def funk_test (begining_bank):
#     test = begining_bank()
#     return (test)
    
# funk_test(begining_bank)
