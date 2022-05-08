n = input("You are in the Lost Forest\n****************\n****************\n:)\n****************\n****************\nGo left or right? ")
c=0
while n == "right" or n == "Right":
    if n=="right" or n=="Right":
        n = input("You are in the Lost Forest\n********************\n********************\n    :) (help me!)»\n********************\n********************\nGo left or right? ")
    if n == "right" or n == "Right":
        n = input("You are in the Lost Forest\n**************************************\n**************************************\n             :) (Try again)»\n**************************************\n**************************************\nGo left or right? ")
    if  n == "right" or n == "Right":
        n = input("You are in the Lost Forest\n*******************************************\n*******************************************\n                       :)  (I think you will not able to help me!)»\n*******************************************\n******************************************\nGo left or right? ")
if n=="Left" or n=="left":
    print("\nYou got out of the Lost Forest!\n\o/")
