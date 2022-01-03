import random

def number():
    rand_numb=[]
    count=0
    while count<4:
        x = random.randint(0,9)
        rand_numb.append(x) #Lägger till slumptalen i en lista
        count+=1
    return rand_numb

def start():
    print("\n")
    print("[1] Start Game")
    print("[2] Exit game")
    print("\n")
    choice=input("What to you want to do? ")
    return choice

def guess(numb, guess_list, new_guess_list, new_numb, right): 
    player_guees=input("guess the number")
    if len(player_guees)>4:
        guess(numb,guess_list, new_guess_list, new_numb, right)
    for i in player_guees:
        i=int(i)
        guess_list.append(i)  
    for n in range(4):  
        if guess_list[n]==numb[n]:
            right+=1
        else:
            new_numb.append(numb[n])
            new_guess_list.append(guess_list[n])
    return right

def check_guess(numb, guess_list, new_guess_list, new_numb):
    nearly=0
    for element in new_guess_list:
        if element in new_numb:
            nearly+=1
    return nearly

choice=start()                          
if choice=='1':
    tries=1
    numb=number()
    right=0
    while right!=4:
        right=0
        guess_list=[]
        new_numb=[]
        new_guess_list=[]
        right=guess(numb,guess_list,new_guess_list, new_numb, right)
        if right==4:
          print("\n","congratulations you guessed all the right numbers,It took ",tries," guesses")
        nearly=check_guess(numb, guess_list, new_guess_list,new_numb )
        print(right, "numbers were in the right position", nearly," is corect but in the wrong position")
        tries+=1