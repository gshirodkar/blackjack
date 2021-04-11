import random
playertotal=0
playercardcount=0
dealercardcount= 0
dealertotal=0
playerbust= False
dealerbust= False
gametie= False
def importantStatements():
    print ("Total number of dealer cards " + str(dealercardcount))
    print ("Total value of dealer cards " + str(dealertotal))
    print ("playercardcount " +str(playercardcount))
    print ("playercardtotal " +str(playertotal))


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
dealerTurn()
importantStatements()
hit()
dealerTurn()
importantStatements()
hit()
dealerTurn()
importantStatements

def stand(): 
    print ("you have have chosen to stand")
def roundCheck():
    global playerbust
    global playertotal
    global dealerbust
    if playertotal >21:
        playerbust= True
    global dealertotal
    if dealertotal >21:
        dealerbust= True
    #put this at the end of the game: if isTie():
        #print ("you tied!, you suck") 
        #check exit game function
    if playerbust:
        print ("dealer wins, you suck")
         #check exit game function
    if dealerbust:
        print ("you win, congrats!")
         #check exit function
roundCheck()


