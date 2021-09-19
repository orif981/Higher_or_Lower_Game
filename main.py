import random
from arts import logo,vs,data,compliments,non_comp
from replit import clear
def check_ans(choice,a_followers,b_followers):
    """checks if the player's guess is correct"""
    if(a_followers>b_followers): return choice=='a'
    else: return choice=='b'

print("Welcome to:")
print()
print(logo)
flag=True
ran_ac2=random.choice(data)
score=0
while flag:
    ran_ac1=ran_ac2
    ran_ac2=random.choice(data)
    while ran_ac2==ran_ac1:
        ran_ac2=random.choice(data)

    print("Compare A: {}, a {} from {}.".format(ran_ac1['name'],ran_ac1['description'],ran_ac1['country']))
    print(vs)
    print("Against B: {}, a {} from {}".format(ran_ac2['name'],ran_ac2['description'],ran_ac2['country']))
    choice=input("Who has more followers? A or B?\n").lower()
    clear()
    print(logo)
    if check_ans(choice,ran_ac1["follower_count"],ran_ac2["follower_count"]):
        score+=1
        print("{}, your score is {}".format(random.choice(compliments),score))
    else:
        print("{}, your final score is: {}".format(random.choice(non_comp),score))
        flag=False




