import random
import string


hint1={
    "raabta":"cast : sushant singh rajput and kriti sanon",
    "dangal":" cast: lead aamir khan ",
    "panga":"cast: kangana ranaut",
    "kesari":"cast :akshay kumar",
    "tanhaji":'cast: ajay devgan and kajol',
    "sholay":"cast: amitabh bachan,and hema malini",
    "padmavat":"cast: ranveer singh and deepika padukone",
    "chichhore":"cast: shraddha kapoor and sushant singh rajput",
    "zero":"cast: shah rukh khan, katrina kaif,Anushka sharma",
    "rab ne bana di jodi":"cast :shah rukh khan and anushka sharma",
    "kuch kuch hota hai":"cast: Shah rukh khan and kajol"

}
hint2={
    "raabta":"movie revolves around a love story and previous life   ",
    "dangal":"biopic on geeta phogat and babita phogat ",
    "panga":"story of a kabbadi player making her comeback after almost 7 years",
    "kesari":"movie based on the historic battle of saragadi",
    "tanhaji":'movie basrd on the  seigh of fort of saragadhi by the maratha empire ',
    "sholay":"the historic movie that gave us the heros like  jai and viru and villans like gaaber singh",
    "padmavat":"cast: a historic drama",
    "zero": "Story of a dwarf person ",
    "chichhore":"movie based on the college life",
    "rab ne bana di jodi":"a story of a punjabi husband who disguise himself himself to win over his wife",
    "kuch kuch hota hai":"cast: story based on college romance"

}

movies=["raabta","dangal","kesari","panga","tanhaji","sholay","padmavat","chichhore","zero","rab ne bana di jodi","kuch kuch hota hai"]
number=random.randint(0,len(movies)-1)
word=movies[number]
game=[]
answer=[]
chances=5
j=0
hint=0
n=0
for i in range(0,len(word)):
    if(word[i]==" "):
        game.append(" ")
        continue

    game.append("*")
    answer.append(word[j])
    j+=1

print("hello this is a guessing game and you have to guess the movie name ")

name=input("please entre you name   :")
print(f'''hi {name} lets play''')
print(f'''your movie is {"".join(game)}''')
while(1):
    print(f'''you have {chances} chances left and {2 - hint} hints left''')
    guess=input("enter your guess letter or enter the name of movie ....if you are not getting the answer type hint :  ")

    if(chances==0):
        print("sorry you ran out of chances please try again")
        break
    if (guess=="".join(answer)):
        print ("yay!you won")
        print('the movie was', word)
        break
    if(guess=="hint" and hint==0):
        print(hint1.get("".join(answer),"no hint avalible"))
        hint+=1
    elif (guess == "hint" and hint == 1):
        print(hint2.get("".join(answer), "no hint avalible"))
        hint += 1
    else:
        n=0
        for i in range(0,len(word)):
            if(guess==answer[i]):
                game[i]=guess
                n+=1

        print("".join(game))
        if(n==0):
            print("sorry there is no matching letter please try again")
            chances=chances-1
        if(game==answer):
            print("yay! you won")
            print('the movie was', word)
            break
