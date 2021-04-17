import random
gamerunning= True
playertotal=0
playercardcount=0
dealercardcount= 0
dealertotal=0
playerbust= False
dealerbust= False
gametie= False
def importantStatements():
    print ("Total number of dealer cards " + str(dealercardcount))
    print ("")
    print ("Total value of dealer cards " + str(dealertotal))
    print ("")
    print ("Total number of player cards " +str(playercardcount))
    print ("")
    print ("Total value of player cards " +str(playertotal))


def getrandomcard():
    return random.randint(1,13)

def isTie():
    if playerbust==dealerbust:
        gametie= True
        print ("It's a tie!")
def dealerTurn():
    global dealercardcount;
    dealercardcount= dealercardcount+1
    global dealertotal;
    dealertotal= getrandomcard()+dealertotal
dealerTurn()

#Prints dealer card stats: - Already used in ImportantStatements Method
# print ("Total number of dealer cards " + str(dealercardcount))
# print ("Total value of dealer cards " + str(dealertotal))

def hit():
    global playercardcount;
    playercardcount+=1
    global playertotal;
    playertotal= getrandomcard()+playertotal
user1= input ("insert name here   ")
print ("generating random card for " +user1)


#Prints player card stats: Already used in ImportantStatements Method
# print ("playercardcount " +str(playercardcount))
# print ("playercardtotal " +str(playertotal))

#Testing with hits!
hit()
#dealerTurn()
importantStatements()

#hit()
#dealerTurn()
#importantStatements()
#hit()
#dealerTurn()
#importantStatements

def roundCheck():
    global playerbust
    global playertotal
    global dealerbust
    if playertotal >21:
        playerbust= True
    global dealertotal
    if dealertotal >21:
        dealerbust= True
    if dealertotal== 21:
        print ("dealer wins, the game is over")
        quit()
    if playertotal== 21:
        print ("player wins, the dealer has lost")
        quit()    
    #put this at the end of the game: if isTie():
        #print ("you tied!, you suck") 
        quit
    if playerbust:
        print ("dealer wins, you suck")
        quit()
    if dealerbust:
        print ("you win, congrats!")
        quit()
roundCheck()

def stand(): 
    global dealertotal
    global playertotal
    while (dealertotal< 16):
        dealerTurn()
        if dealertotal>16 or dealertotal<21:
            importantStatements()
            if dealertotal> playertotal:
                print ("you lose")
            if dealertotal< playertotal:
                print ("you win")
            quit()
    roundCheck()
    importantStatements()
    print ("you have chosen to stand")
    if dealertotal> playertotal:
        print ("you lose")
    if dealertotal< playertotal:
        print ("you win")
    quit()



while(gamerunning):
    userinput= input ("do you want to hit or stand?   ")
    if userinput == "hit":
        hit()
        dealerTurn()
    if userinput== "stand":
        stand()
        dealerTurn()
    importantStatements()
    roundCheck()
    
#if userinput!= "hit" or userinput!= "stand":
   # print ("")
   # print ("you idiot insert hit or stand")
   # userinput= input ("do you want to hit or stand?   ")






