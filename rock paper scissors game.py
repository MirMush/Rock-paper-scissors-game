import random

user= input(" rock , paper or scissors?")
L=["rock","paper","scissors"]
result=(random.choice(L))
print (" you chose ", user ," and computer chose", result )

    
if user == result:
    print(" it's a draw!")
elif user=="rock":
    if result== "scissors":
        print(" you win")
    else :
        print ( "you lose")
elif user=="paper":
    if result== "scissors":
        print(" you lose")
    else :
        print ( "you win")
elif user=="scissors":
    if result== "rock":
        print(" you lose")
    else :
        print ( "you win")



        

