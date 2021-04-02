import random
playertotal=0
playercardcount=0
dealercardcount= 0
dealertotal=0
playerbust= False
dealerbust= False
gametie= False
def isBust():
    if playertotal >21:
        playerbust= True
    if dealertotal >21:
        dealerbust= True
def isTie():
    if playerbust==dealerbust:
        gametie= True
        print ("It's a tie!")
def getrandomcard():
    return random.randint(1,13)
print (playercardcount)
#def hit():
    #playercardcount+=1
    #playertotal= getrandomcard()+playertotal
user1= input ("insert name here   ")
print ("generating random card for " +user1)
#hit()
print (playertotal)
print (playercardcount)
   
