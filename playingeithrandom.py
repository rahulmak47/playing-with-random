import random

print("welcome to fun zone")
print("here you can play two types of game")
print("1.playing with random number")
print("2.guess the correct name")
totalmoney=5000
turn=0
history={}
while(turn<5):
    print("select 1 for random number game and 2 for guess the name game")
    mode=int(input())
    val = 0
    if(mode==1):

        rand = random.randint(0, 100)
        count = 1
        flag = 0
        for i in range(1, 11):
            print("enter the number")
            num = int(input())
            if (num == rand):
                print(f"you take  {count} tries to win the game")
                flag = 1
                break;
            elif (num > rand):
                print("you select big number please select smallest number")
            else:
                print("you select small number please select big number")
            count = count + 1

        if (flag == 0):
            print("you lose the game and you lose 1000 rs")
            val=-1000
            totalmoney=totalmoney-1000
        if (count <= 4):
            print("you earn 5000 rs")
            totalmoney = totalmoney + 4000
            val=4000
        elif (count > 4 and count <= 7):
            totalmoney = totalmoney + 1500
            val=1500
            print("you earn 2500 rs")
        elif (count >= 7 and flag == 1):
            totalmoney = totalmoney + 500
            val=500
            print("you earn 1500 rs")
        if(val==0):
            history[turn]="you lose 1000 rs in plying with randome number game"
        else:
            history[turn] = f"you earn {val} rs in plying with randome number game"

    else:
        player = ["Rahul","Milan","Sagar","Chintan","Chirag","Vivek","Nitin","Dipak","Sanjay","Ravi","Prakash"]
        flag1 = 0
        ans = random.choice(player)
        for i in range(0, 5):
            print(f"guess  the player name which taken by the computer from the {player}")
            ans1 = input()
            if (ans == ans1):
                print("you select the correct player")
                flag1 = 1
                break
        if (flag1 == 0):
            print(f"oops's you lose the game better luck next time \n selected player is {ans}")
            totalmoney=totalmoney-1000
            val=-1000
        else:
            print("congratulation you guess the correct name you win 3000 rs ")
            totalmoney=totalmoney+2000
            val=2000
        if (val < 0):
            history[turn] = "you lose 1000 rs in guess the correct name game"
        else:
            history[turn] = f"you earn {val} rs in guess the correct name game"
    turn=turn+1
diff=totalmoney-5000
print("it is the history of you game")
for i,j in history.items():
    print (f"in  game {i+1}"
           f" {j} ")
if(diff>0):
    print(f"your total profit is  {diff} rs")
elif(diff<0):
    print(f"you total loss is {diff} rs")
else:
    print("there is no loss and no profit")




