import random

class attack:
    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getdmg(self):
        return random.randrange(self.atkl,self.atkh)

def hpbar(hpp,name):
    bar=""
    hppInt=hpp/2
    for x in range(int(hppInt)):
        bar+="█"

    blankspacecount=50-len(bar)
    blankspace=""

    for x in range(blankspacecount):
        blankspace+=" "

    #print("                  __________________________________________________")
    print(name+" HP :"+str(hpp)+"/100"+"|"+bar+blankspace+"|")





pistol=attack(0,20)
ak47=attack(0,30)
thanoshit=attack(0,60)

playerhp=100
thanoshp=100
#3 medkits fills 50hp to player
#3 ak attack 5 pistol attacks
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to Battle Game!"
      "\nYou have 5 bullets of pistol, 3 bullets of AK47 and 3 medkits which heals for 50 points."
      "\nAlternative attacks by the player and opponent.\nMax HP Player :100, Max HP thanos :",thanoshp,"\nGo kill him!!\n\n1.Pistol Attack, 2.AK47 Attack, 3.Heal")

running= True
heal_count=0
akcount=0
pistolcount=0
while running:
    print("========================================================================================================")
    attack_choice = int(input("Choose the action : "))

    if attack_choice == 1:
        if pistolcount < 5:
            # print("You are attacking with Pistol")
            playerdmg = pistol.getdmg()
            pistolcount = pistolcount + 1
            thanoshp = thanoshp - playerdmg
            if thanoshp < 0:
                thanoshp = 0
            print("You attacked thanos with pistol! Damaged him with ", playerdmg, "points.")
            if thanoshp == 0:
                print("You won!! ")
                break
            thanosdmg = thanoshit.getdmg()
            playerhp = playerhp - thanosdmg
            if playerhp < 0:
                playerhp = 0
            print("Thanos attacked you back! Damaged with ", thanosdmg, " points. \nPlayerHP:", playerhp,", ThanosHP:",thanoshp,", Pistol bullets left: ",5-pistolcount,", Ak47 bullets left:",3-akcount,", Medkits left:",3-heal_count)
            hpbar(playerhp,"Player")
            hpbar(thanoshp,"Thanos")
        else:
            print("Pistol bullets are empty!!")




    elif attack_choice == 2:
        if akcount < 3:
            # print("You are attacking with Ak47")
            playerdmg = ak47.getdmg()
            akcount=akcount+1
            thanoshp = thanoshp - playerdmg
            if thanoshp < 0:
                thanoshp = 0
            print("You attacked thanos with AK47! Damaged him with ", playerdmg, "points.")
            if thanoshp == 0:
                print("You won!! ")
                break
            thanosdmg = thanoshit.getdmg()
            playerhp = playerhp - thanosdmg
            if playerhp < 0:
                playerhp = 0
            print("Thanos attacked you back! Damaged with ", thanosdmg, " points. \nPlayerHP:", playerhp,", ThanosHP:",thanoshp,", Pistol bullets left : ",5-pistolcount,", Ak47 bullets left :",3-akcount,", Medkits left:",3-heal_count)
            hpbar(playerhp, "Player")
            hpbar(thanoshp, "Thanos")
        else:
            print("Ak47 bullets are empty!!")



    elif attack_choice == 3:
        if heal_count <3:
            #print("You are getting healed with 50 HP")
            if playerhp <= 50:
                playerhp = playerhp + 50
            else:
                playerhp = 100
            heal_count=heal_count+1
            print("You got healed with 50 HP.\nPlayerHP:", playerhp,", ThanosHP:",thanoshp,", Pistol bullets left:",5-pistolcount,", Ak47 bullets left :",3-akcount,", Medkits left:",3-heal_count)
            hpbar(playerhp, "Player")
            hpbar(thanoshp, "Thanos")
        else:
            print("Medkits are Empty!\n")

    else:
        print("Invalid Action")


    if playerhp == 0:
        print("<-----Thanos defeated you! Game Over!!----->")
        running = False
        break

    if akcount == 3 and pistolcount == 5 and heal_count == 3:
        print("\nYou are out of actions!")
        if playerhp > thanoshp:
            print("You have more HP, YOU WON!!")

        else:
            print("Thanos has more HP, You Lost!! Game Over!")

        break








