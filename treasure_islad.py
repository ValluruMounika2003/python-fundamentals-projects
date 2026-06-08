print("""
---------------------------------------.---------.
|                                       |         |
|    ,-----------------------------.    |    .    |
|    |                             |    |    |    |
|    |    ,-------------------.    |    |    |    |
|    |    |                   |    |    |    |    |
|    |    `----     ,----     |    |    |    |    |
|    |              | X       |    |    |    |    |
|    |    ,---------"---------:    |    `----'    |
|    |    |                   |    |              |
|    `----:    ,---------.    |    `---------.    |
|         |    |         |    |              |    |
|    .    |    |    .    |    |     ---------'    |
|    |    |    |    |    |    |                   |
:----'    |    |    |    |    |    ,--------------:
|         |    |    |    |    |    |              |
|    .    |    `----'    |    |    |     ----.    |
|    |    |              |    |    |         |    |
|    `----"---------     |    |    `---------'    |
|                        |    |                   |
`------------------------'    `-------------------'
""")
print("welcome to Treasure Island")
print("your mission is to find the treasure.")
road = input("you're at a cross road. where do you to go ? is it a left or right ? ")
if road == "left":
    swim = input("do you what to swim or wait for the boart ")
    if swim == "wait":
        door= input("what  type of the door do you choose red ,yellow,green ")
        if door == "red":
            print("you won the treasure")
        elif door == "yellow":
            print("you are fight by the Queen Elinor")
        else:
            print("you are fight by the Mulan")
    else:
        print("Attacked by trout.Game Over.")
else:
    print ("Fall into a hole.Game Over.")