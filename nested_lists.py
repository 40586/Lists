#Kieran Burnett
#06-01-2015
#Lists of lists
player = [
    ["k1llmAchine",51,49],
    ["bob2247",5 , 99],
    ["hAxOr12",72,30]
]



print("|{0:<12}|{1:<3}|{2:<3}|".format("Name","Kills","Deaths"))
print("-"*27)
for play in player:
    print("|{0:<12}|{1:<5}|{2:<6}|".format(play[0],play[1],play[2]))
    print("-"*27)
