#Pokemon Dicelocke Dice Roller beta 0.025 by Jmsnipes100(Jacob M. Snipes)
print("Welcome to the Pokemon Dicelocke Dice Roller by Jmsnipes100!")
import random
print(" ")
print("For help type 'Help', for rules type 'Rules'.")
print(" ")
print("Entering anything but a # when asked for will cause the Dice Roller to crash.")
while 1==1:
    print(" ")
    function=input("What do you need? ")
    if function == "Starter":
        roll=int(random.randint(1,3))
        if roll==1:
            print("Your Starter is a Grass type!")
        elif roll==2:
            print("Your Starter is a Fire type!")
        elif roll==3:
            print("Your Starter is a Water type!")
        else:
            print("ERROR")
    elif function=="Capture":
        party=int(input("How many pokemon are in your party? "))
        roll=int(random.randint(1,6)-party)
        if roll>0:
            print("You can attempt to capture the pokemon.")
        elif roll<1:
            print("You cannot attempt to capture the pokemon.")
        else:
            print("ERROR")
    elif function=="New Town":
        roll=str(random.randint(1,12))
        print("You may buy "+roll+" item(s) in this town.")
    elif function=="Item":
        party=int(input("How many pokemon are in your party? "))
        roll=int(random.randint(1,6)+party)
        if roll>6:
            print("You can keep the item")
        elif roll<7:
            print("You must discard the item.")
        else:
            print("ERROR")
    elif function=="Revive":
        party=int(input("How many pokemon where in your party at the time of your gym victory? "))
        roll=int(random.randint(1,6)-party)
        if roll>0:
            print("You many revive one of your pokemon!")
        elif roll<1:
            print("You cannot revive one of your pokemon.")
        else:
            print("ERROR")
    elif function=="Help":
        print(" ")
        print("Starter: Choses your starter.")
        print(" ")
        print("Capture: Determines if you can capture the pokemon you encountered.\n(You have 3 chances, the Dice Roller does not keep track of them)")
        print(" ")
        print("Item: Determines if you can keep the item you found.")
        print(" ")
        print("New Town: Determines how many items you can buy at the mart.(The Dice Roller \ndoes not keep track of the # of items you can buy)")
        print(" ")
        print("Revive: Gives you a chance to revive a pokemon in your graveyard after \nbeating a gym.(Revives cannot be saved)")
        print(" ")
        print("Name: Generates a name for your pokemon.")
        print(" ")
        print("Help: List the functions of the commands.")
        print(" ")
        print("Rules: Lists the basic rules of Dicelocke.")
    elif function=="Rules":
        print("1:You must use the 'Starter' function to chose your starter.")
        print("")
        print("2:You must use the 'Name' function to name your pokemon.\n(Note there is a slight chance that a name will be profane/insulting\n & you can then change it if you wish by running the 'Name' function again)")
        print("")
        print("3:You must use the 'Capture' function on the first pokemon \nyou encounter in an area except when that pokemon is a duplicate \nor evolution of a pokemon you have. When the Dice Roller says you cannot \ncapture the pokemon you defeat it or exit the battle and try again. \nOn the third time the Dice Roller says you cannot caputre the pokemon \nthen you cannot capture a pokemon in that area. \nIf the Dice Roller says you can capture the pokemon and you fail to capture it \nyou cannot capture a pokemon in that area.")
        print("")
        print("4:If you enounter the same pokemon that you have/is an evolution \nof a pokemon you have 3 times in a new area you cannot capture a \npokemon in that area.")
        print("")
        print("5:All pokemon that faint go into a pc box marked Grave.")
        print("")
        print("6:You must use the 'Revive' function after beating a gym leader \nonly if you have a dead pokemon in your party or 'Grave' box.")
        print("")
        print("7:You must use the 'New Town' function when you reach a new town \nto ditermin how many items you can buy from the mart of that town.")
        print("")
        print("8:You must use the 'Item' function when you pick an item off the ground \nto see if you can keep it, you must discard it when the \nDice Roller says you cannot keep it.")
        print("")
        print("9:No trading with anyone with anyone except with NPCs.")
        print("")
        print("10:You cannot put pokemon in the daycare but you can receive eggs \nthat you did not come from your pokemon in a daycare.")
        print("")
        print("10:You lose the Dicelocke challenge when all pokemon you have no \nliving pokemon in your party or pc.")
        print("")
        print("11:You can add any additional rules to your challenge that does not \nconflict with the first 11 rules.")
    elif function=="Name":
        length=int(random.randint(1,12))
        N1=random.randint(1,26)
        if N1==1:
            N1="A"
        elif N1==2:
            L1="B"
        elif N1==3:
            L1="C"
        elif N1==4:
            L1="D"
        elif N1==5:
            L1="E"
        elif N1==6:
            L1="F"
        elif N1==7:
            L1="G"
        elif N1==8:
            L1="H"
        elif N1==9:
            L1="I"
        elif N1==10:
            L1="J"
        elif N1==11:
            L1="K"
        elif N1==12:
            L1="L"
        elif N1==13:
            L1="M"
        elif N1==14:
            L1="N"
        elif N1==15:
            L1="O"
        elif N1==16:
            L1="P"
        elif N1==17:
            L1="Q"
        elif N1==18:
            L1="R"
        elif N1==19:
            L1="S"
        elif N1==20:
            L1="T"
        elif N1==21:
            L1="U"
        elif N1==22:
            L1="V"
        elif N1==23:
            L1="W"
        elif N1==24:
            L1="X"
        elif N1==25:
            L1="Y"
        elif N1==26:
            L1="Z"
        else:
            print("ERROR")
        N2=random.randint(1,26)
        if N2==1:
            L2="a"
        elif N2==2:
            L2="b"
        elif N2==3:
            L2="c"
        elif N2==4:
            L2="d"
        elif N2==5:
            L2="e"
        elif N2==6:
            L2="f"
        elif N2==7:
            L2="g"
        elif N2==8:
            L2="h"
        elif N2==9:
            L2="i"
        elif N2==10:
            L2="j"
        elif N2==11:
            L2="k"
        elif N2==12:
            L2="l"
        elif N2==13:
            L2="m"
        elif N2==14:
            L2="n"
        elif N2==15:
            L2="o"
        elif N2==16:
            L2="p"
        elif N2==17:
            L2="q"
        elif N2==18:
            L2="r"
        elif N2==19:
            L2="s"
        elif N2==20:
            L2="t"
        elif N2==21:
            L2="u"
        elif N2==22:
            L2="v"
        elif N2==23:
            L2="w"
        elif N2==24:
            L2="x"
        elif N2==25:
            L2="y"
        elif N2==26:
            L2="z"
        else:
            print("ERROR")
        N3=random.randint(1,26)
        if N3==1:
            L3="a"
        elif N3==2:
            L3="b"
        elif N3==3:
            L3="c"
        elif N3==4:
            L3="d"
        elif N3==5:
            L3="e"
        elif N3==6:
            L3="f"
        elif N3==7:
            L3="g"
        elif N3==8:
            L3="h"
        elif N3==9:
            L3="i"
        elif N3==10:
            L3="j"
        elif N3==11:
            L3="k"
        elif N3==12:
            L3="l"
        elif N3==13:
            L3="m"
        elif N3==14:
            L3="n"
        elif N3==15:
            L3="o"
        elif N3==16:
            L3="p"
        elif N3==17:
            L3="q"
        elif N3==18:
            L3="r"
        elif N3==19:
            L3="s"
        elif N3==20:
            L3="t"
        elif N3==21:
            L3="u"  
        elif N3==22:
            L3="v"
        elif N3==23:
            L3="w"
        elif N3==24:
            L3="x"
        elif N3==25:
            L3="y"
        elif N3==26:
            L3="z"
        else:
          print("ERROR")
        N4=random.randint(1,26)
        if N4==1:
            L4="a"
        elif N4==2:
            L4="b"
        elif N4==3:
            L4="c"
        elif N4==4:
            L4="d"
        elif N4==5:
            L4="e"
        elif N4==6:
            L4="f"
        elif N4==7:
            L4="g"
        elif N4==8:
            L4="h"
        elif N4==9:
            L4="i"
        elif N4==10:
            L4="j"
        elif N4==11:
            L4="k"
        elif N4==12:
            L4="l"
        elif N4==13:
            L4="m"
        elif N4==14:
            L4="n"
        elif N4==15:
            L4="o"
        elif N4==16:
            L4="p"
        elif N4==17:
            L4="q"
        elif N4==18:
            L4="r"
        elif N4==19:
            L4="s"
        elif N4==20:
            L4="t"
        elif N4==21:
            L4="u"
        elif N4==22:
            L4="v"
        elif N4==23:
            L4="w"
        elif N4==24:
            L4="x"
        elif N4==25:
            L4="y"
        elif N4==26:
            L4="z"
        else:
            print("ERROR")
        N5=random.randint(1,26)
        if N5==1:
            L5="a"
        elif N5==2:
            L5="b"
        elif N5==3:
            L5="c"
        elif N5==4:
            L5="d"
        elif N5==5:
            L5="e"
        elif N5==6:
            L5="f"
        elif N5==7:
            L5="g"
        elif N5==8:
            L5="h"
        elif N5==9:
            L5="i"
        elif N5==10:
            L5="j"
        elif N5==11:
            L5="k"
        elif N5==12:
            L5="l"
        elif N5==13:
            L5="m"
        elif N5==14:
            L5="n"
        elif N5==15:
            L5="o"
        elif N5==16:
            L5="p"
        elif N5==17:
            L5="q"
        elif N5==18:
            L5="r"
        elif N5==19:
            L5="s"
        elif N5==20:
            L5="t"
        elif N5==21:
            L5="u"
        elif N5==22:
            L5="v"
        elif N5==23:
            L5="w"
        elif N5==24:
            L5="x"
        elif N5==25:
            L5="y"
        elif N5==26:
            L5="z"
        else:
          print("ERROR")
        N6=random.randint(1,26)
        if N6==1:
            L6="a"
        elif N6==2:
            L6="b"
        elif N6==3:
            L6="c"
        elif N6==4:
            L6="d"
        elif N6==5:
            L6="e"
        elif N6==6:
            L6="f"
        elif N6==7:
            L6="g"
        elif N6==8:
            L6="h"
        elif N6==9:
            L6="i"
        elif N6==10:
            L6="j"
        elif N6==11:
            L6="k"
        elif N6==12:
            L6="l"
        elif N6==13:
            L6="m"
        elif N6==14:
            L6="n"
        elif N6==15:
            L6="o"
        elif N6==16:
            L6="p"
        elif N6==17:
            L6="q"
        elif N6==18:
            L6="r"
        elif N6==19:
            L6="s"
        elif N6==20:
            L6="t"
        elif N6==21:
            L6="u"
        elif N6==22:
            L6="v"
        elif N6==23:
            L6="w"
        elif N6==24:
            L6="x"
        elif N6==25:
            L6="y"
        elif N6==26:
            L6="z"
        else:
            print("ERROR")
        N7=random.randint(1,26)
        if N7==1:
            L7="a"
        elif N7==2:
            L7="b"
        elif N7==3:
            L7="c"
        elif N7==4:
            L7="d"
        elif N7==5:
            L7="e"
        elif N7==6:
            L7="f"
        elif N7==7:
            L7="g"
        elif N7==8:
            L7="h"
        elif N7==9:
            L7="i"
        elif N7==10:
            L7="j"
        elif N7==11:
            L7="k"
        elif N7==12:
            L7="l"
        elif N7==13:
            L7="m"
        elif N7==14:
            L7="n"
        elif N7==15:
            L7="o"
        elif N7==16:
            L7="p"
        elif N7==17:
            L7="q"
        elif N7==18:
            L7="r"
        elif N7==19:
            L7="s"
        elif N7==20:
            L7="t"
        elif N7==21:
            L7="u"
        elif N7==22:
            L7="v"
        elif N7==23:
            L7="w"
        elif N7==24:
            L7="x"
        elif N7==25:
            L7="y"
        elif N7==26:
            L7="z"
        else:
            print("ERROR")
        N8=random.randint(1,26)
        if N8==1:
            L8="a"
        elif N8==2:
            L8="b"
        elif N8==3:
            L8="c"
        elif N8==4:
            L8="d"
        elif N8==5:
            L8="e"
        elif N8==6:
            L8="f"
        elif N8==7:
            L8="g"
        elif N8==8:
            L8="h"
        elif N8==9:
            L8="i"
        elif N8==10:
            L8="j"
        elif N8==11:
            L8="k"
        elif N8==12:
            L8="l"
        elif N8==13:
            L8="m"
        elif N8==14:
            L8="n"
        elif N8==15:
            L8="o"
        elif N8==16:
            L8="p"
        elif N8==17:
            L8="q"
        elif N8==18:
            L8="r"
        elif N8==19:
            L8="s"
        elif N8==20:
            L8="t"
        elif N8==21:
            L8="u"
        elif N8==22:
            L8="v"
        elif N8==23:
            L8="w"
        elif N8==24:
            L8="x"
        elif N8==25:
            L8="y"
        elif N8==26:
            L8="z"
        else:
            print("ERROR")
        N9=random.randint(1,26)
        if N9==1:
            L9="a"
        elif N9==2:
            L9="b"
        elif N9==3:
            L9="c"
        elif N9==4:
            L9="d"
        elif N9==5:
            L9="e"
        elif N9==6:
            L9="f"
        elif N9==7:
            L9="g"
        elif N9==8:
            L9="h"
        elif N9==9:
            L9="i"
        elif N9==10:
            L9="j"
        elif N9==11:
            L9="k"
        elif N9==12:
            L9="l"
        elif N9==13:
            L9="m"
        elif N9==14:
            L9="n"
        elif N9==15:
            L9="o"
        elif N9==16:
            L9="p"
        elif N9==17:
            L9="q"
        elif N9==18:
            L9="r"
        elif N9==19:
            L9="s"
        elif N9==20:
            L9="t"
        elif N9==21:
            L9="u"
        elif N9==22:
            L9="v"
        elif N9==23:
            L9="w"
        elif N9==24:
            L9="x"
        elif N9==25:
            L9="y"
        elif N9==26:
            L9="z"
        else:
            print("ERROR")
        N10=random.randint(1,26)
        if N10==1:
            L10="a"
        elif N10==2:
            L10="b"
        elif N10==3:
            L10="c"
        elif N10==4:
            L10="d"
        elif N10==5:
            L10="e"
        elif N10==6:
            L10="f"
        elif N10==7:
            L10="g"
        elif N10==8:
            L10="h"
        elif N10==9:
            L10="i"
        elif N10==10:
            L10="j"
        elif N10==11:
            L10="k"
        elif N10==12:
            L10="l"
        elif N10==13:
            L10="m"
        elif N10==14:
            L10="n"
        elif N10==15:
            L10="o"
        elif N10==16:
            L10="p"
        elif N10==17:
            L10="q"
        elif N10==18:
            L10="r"
        elif N10==19:
            L10="s"
        elif N10==20:
            L10="t"
        elif N10==21:
            L10="u"
        elif N10==22:
            L10="v"
        elif N10==23:
            L10="w"
        elif N10==24:
            L10="x"
        elif N10==25:
            L10="y"
        elif N10==26:
            L10="z"
        else:
            print("ERROR")
        N11=random.randint(1,26)
        if N11==1:
            L11="a"
        elif N11==2:
            L11="b"
        elif N11==3:
            L11="c"
        elif N11==4:
            L11="d"
        elif N11==5:
            L11="e"
        elif N11==6:
            L11="f"
        elif N11==7:
            L11="g"
        elif N11==8:
            L11="h"
        elif N11==9:
            L11="i"
        elif N11==10:
            L11="j"
        elif N11==11:
            L11="k"
        elif N11==12:
            L11="l"
        elif N11==13:
            L11="m"
        elif N11==14:
            L11="n"
        elif N11==15:
            L11="o"
        elif N11==16:
            L11="p"
        elif N11==17:
            L11="q"
        elif N11==18:
            L11="r"
        elif N11==19:
            L11="s"
        elif N11==20:
            L11="t"
        elif N11==21:
            L11="u"
        elif N11==22:
            L11="v"
        elif N11==23:
            L11="w"
        elif N11==24:
            L11="x"
        elif N11==25:
            L11="y"
        elif N11==26:
            L11="z"
        else:
            print("ERROR")
        N12=random.randint(1,26)
        if N12==1:
            L12="a"
        elif N12==2:
            L12="b"
        elif N12==3:
            L12="c"
        elif N12==4:
            L12="d"
        elif N12==5:
            L12="e"
        elif N12==6:
            L12="f"
        elif N12==7:
            L12="g"
        elif N12==8:
            L12="h"
        elif N12==9:
            L12="i"
        elif N12==10:
            L12="j"
        elif N12==11:
            L12="k"
        elif N12==12:
            L12="l"
        elif N12==13:
            L12="m"
        elif N12==14:
            L12="n"
        elif N12==15:
            L12="o"
        elif N12==16:
            L12="p"
        elif N12==17:
            L12="q"
        elif N12==18:
            L12="r"
        elif N12==19:
            L12="s"
        elif N12==20:
            L12="t"
        elif N12==21:
            L12="u"
        elif N12==22:
            L12="v"
        elif N12==23:
            L12="w"
        elif N12==24:
            L12="x"
        elif N12==25:
            L12="y"
        elif N12==26:
            L12="z"
        else:
            print("ERROR")
        name=L1+L2+L3+L4+L5+L6+L7+L8+L9+L10+L11+L12
        print("Your pokemon's name is, "+name[:length]+"!")
    else:
        print("No such function.")
